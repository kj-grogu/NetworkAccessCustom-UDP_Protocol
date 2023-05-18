import socket
from packets import *
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
CLIENT_ID = 0x01
MESSAGE =  "Payload message part : "

# Send the data packet
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

TIMEOUT = 3
MAX_RETRIES = 3

def make_request_with_retry(data_packet_bytes):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(TIMEOUT)
    attempt = 0
    for i in range(MAX_RETRIES):
        print(f'Sending message to server, attempt: {i+1}')
        attempt += 1
        # send data to server
        client_socket.sendto(data_packet_bytes, (UDP_IP, UDP_PORT))

        try:
            data, address = client_socket.recvfrom(1024)
            print(data)
            packet_type = hex(int.from_bytes(data[3:5], byteorder='big'))
            if packet_type == "0xfff3":
                print("REJECT")
                rej_packet = REJECT_PACKET.from_bytes(data)
                print("====================")
                print(rej_packet)
                print("====================")
            elif packet_type == "0xfff2":
                print("ACK")
                ack_packet = ACK_PACKET.from_bytes(data)
                print("====================")
                print(ack_packet)
                print("====================")
            else:
                print("Unknown Type of packet")
            break  # break the loop if the response is received successfully
        except socket.timeout:
            print(f'Attempt: {i+1} failed')

    if attempt == 3:
        print(f'Error - Server does not respond')
    client_socket.close()



###### GOOD loop
for i in range(1,6):
    msg_to_send = MESSAGE+str(i)
    data_packet = DATA_PACKET(client_id = CLIENT_ID, segment_id = i, total_len = len(msg_to_send), payload = msg_to_send)
    print(data_packet)
    make_request_with_retry(data_packet.to_bytes())
    time.sleep(1)



# ## First successful
msg_to_send = MESSAGE+str(1)+"reset"
data_packet = DATA_PACKET(client_id = CLIENT_ID, segment_id = 1, total_len = len(msg_to_send), payload = msg_to_send)
print(data_packet)
make_request_with_retry(data_packet.to_bytes())
time.sleep(3)

# ### CASE 1 Out of sequence
msg_to_send = MESSAGE+str(3)
data_packet = DATA_PACKET(client_id = CLIENT_ID, segment_id = 3, total_len = len(msg_to_send), payload = msg_to_send)
print(data_packet)
make_request_with_retry(data_packet.to_bytes())
time.sleep(3)


# ### CASE 2 Message Length doesnt match
msg_to_send = MESSAGE+str(1)
data_packet = DATA_PACKET(client_id = CLIENT_ID, segment_id = 1, total_len = 99, payload = msg_to_send)
print(data_packet)
make_request_with_retry(data_packet.to_bytes())
time.sleep(3)

### CASE 3 Malformed packet
msg_to_send = MESSAGE+str(2)
data_packet = DATA_PACKET(client_id = CLIENT_ID, segment_id = 1, total_len = len(msg_to_send), payload = msg_to_send)
data_packet_bytes = data_packet.to_bytes()
data_packet_bytes = data_packet_bytes[0:-8]
print("Malformed")
print(data_packet_bytes)
make_request_with_retry(data_packet_bytes)
time.sleep(3)


# ### CASE 4 Duplicate
msg_to_send = MESSAGE+str(2)
data_packet = DATA_PACKET(client_id = CLIENT_ID, segment_id = 1, total_len = len(msg_to_send), payload = msg_to_send)
print(data_packet)
make_request_with_retry(data_packet.to_bytes())