import socket
from packets import *

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("UDP server up and listening...")
segmentIndex = 1
received_packets = set()

while True:
    try:
        data, addr = sock.recvfrom(1024)
        print(addr)
        data_packet = None
        try:
            data_packet = DATA_PACKET.from_bytes(data)
        except Exception as e:
            print("Exception while reading packet")
            print(e)
            print("End of packet missing")
            client_id = data[2]
            segment_id = data[5]
            rej = REJECT_PACKET(client_id, segment_id,
                                REJECT_PACKET.REJECT_CODE_END_OF_PACKET_MISSING)
            print("====================")
            print(rej)
            print("====================")
            rej_bytes = rej.to_bytes()
            sock.sendto(rej_bytes, addr)

            # continue

        if data_packet == None:
            continue
        print("====================")
        print(data_packet)
        print("====================")

        ## ### handling logic
        ## RESET
        if (data_packet.payload.endswith("reset")):
            # print("resetting...")
            segmentIndex = 1
            received_packets = set()

        ## Len dont match
        if (data_packet.total_len != len(data_packet.payload)):
            print("REJECTING : length doesnt match")
            rej = REJECT_PACKET(data_packet.client_id, data_packet.segment_id,
                                REJECT_PACKET.REJECT_CODE_LENGTH_MISMATCH)
            rej_bytes = rej.to_bytes()
            sock.sendto(rej_bytes, addr)

        ## Duplicate
        elif (data_packet.segment_id in received_packets):
            print("REJECTING : duplicate")
            rej = REJECT_PACKET(data_packet.client_id, data_packet.segment_id,
                                REJECT_PACKET.REJECT_CODE_DUPLICATE_PACKET)
            rej_bytes = rej.to_bytes()
            sock.sendto(rej_bytes, addr)

        ## Out of Sequence
        elif (data_packet.segment_id != segmentIndex):
            print("REJECTING : out of sequence")
            rej = REJECT_PACKET(data_packet.client_id, data_packet.segment_id,
                                REJECT_PACKET.REJECT_CODE_OUT_OF_SEQUENCE)
            rej_bytes = rej.to_bytes()
            sock.sendto(rej_bytes, addr)

        else:  # VALID
            print("[ACK]")
            ack = ACK_PACKET(data_packet.client_id, data_packet.segment_id)
            ack_bytes = ack.to_bytes()
            sock.sendto(ack_bytes, addr)
            segmentIndex += 1
            received_packets.add(data_packet.segment_id)
    except Exception as e:
        print("An exception occurred:", e)