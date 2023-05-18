import socket
from packets import *
import time
import sys

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
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

        # send data to server
        client_socket.sendto(data_packet_bytes, (UDP_IP, UDP_PORT))

        try:
            data, address = client_socket.recvfrom(1024)
            print(data)
            packet_type = hex(int.from_bytes(data[3:5], byteorder='big'))
            print(packet_type)
            if packet_type == "0xfffb":
                print("ACCESS_PERMITTED_PACKET")
                # rej_packet = REJECT_PACKET.from_bytes(data)
                acc_permitted_packet = ACCESS_PERMITTED_PACKET.from_bytes(data)
                print("====================")
                print(acc_permitted_packet)
                print("====================")
            elif packet_type == "0xfffa":
                print("SUBSCRIBER_DOESNOT_EXIST_PACKET")
                sub_doesnt_exist_packet = SUBSCRIBER_DOESNOT_EXIST_PACKET.from_bytes(data)
                print("====================")
                print(sub_doesnt_exist_packet)
                print("====================")
            elif packet_type == "0xfff9":
                print("SUBSCRIBER_NOT_PAID_PACKET")
                sub_not_paid_packet = SUBSCRIBER_NOT_PAID_PACKET.from_bytes(data)
                print("====================")
                print(sub_not_paid_packet)
                print("====================")
            else:
                print("Unknown Type of packet")
            break  # break the loop if the response is received successfully
        except socket.timeout:
            print(f'Attempt: {i+1} failed')

    if attempt == 3:
        print(f'Error - Server does not respond')
    client_socket.close()


# # ## Subscriber Not Found
acc_perm_packet = ACCESS_PERMISSION_PACKET(client_id = 99, segment_id = 1, total_len = 1, technology = Technologies["2G"], source_subscriber_no= 4086808822)
print(acc_perm_packet)
make_request_with_retry(acc_perm_packet.to_bytes())
time.sleep(1)



# ## Subscriber Found but tech doesnt match
acc_perm_packet = ACCESS_PERMISSION_PACKET(client_id = 99, segment_id = 1, total_len = 1, technology = Technologies["4G"], source_subscriber_no= 4086808821)
print(acc_perm_packet)
make_request_with_retry(acc_perm_packet.to_bytes())
time.sleep(1)


# ## Subscriber Found but not paid
acc_perm_packet = ACCESS_PERMISSION_PACKET(client_id = 99, segment_id = 1, total_len = 1, technology = Technologies["3G"], source_subscriber_no= 4086668821)
print(acc_perm_packet)
make_request_with_retry(acc_perm_packet.to_bytes())
time.sleep(1)


# ## Subscriber Found and paid
acc_perm_packet = ACCESS_PERMISSION_PACKET(client_id = 99, segment_id = 1, total_len = 1, technology = Technologies["2G"], source_subscriber_no= 4086808821)
print(acc_perm_packet)
make_request_with_retry(acc_perm_packet.to_bytes())
time.sleep(1)
