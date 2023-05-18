import socket
from packets import *
import traceback

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("UDP server up and listening...")
segmentIndex = 1
received_packets = set()

def read_subscriber(sub_id, tech):
    with open('Verification_Database.txt', 'r') as file:
        next(file)
        line = file.readline()
        msg = "Not_Found"
        while line:
            arr = line.split()
            if(arr[0] == str(sub_id)): ### match the subscriber no
                if(int(arr[1]) == int(tech)): ### match the TECH
                    if(arr[2] == str(1)): ### Check If paid
                        return "Valid"
                    else:
                        return "Not_Paid"
                else:
                    msg = "Tech_Mismatch"
            line = file.readline()
    return msg

while True:
    try:
        data, addr = sock.recvfrom(1024)
        print(addr)

        acc_perm_packet = ACCESS_PERMISSION_PACKET.from_bytes(data)
        print("====================")
        print(acc_perm_packet)
        print("====================")

        res = read_subscriber(acc_perm_packet.source_subscriber_no, acc_perm_packet.technology)
        print(res)
        if(res == "Valid"):
            acc_permited_packet = ACCESS_PERMITTED_PACKET(client_id = acc_perm_packet.client_id, segment_id = acc_perm_packet.segment_id, total_len = 1, technology = acc_perm_packet.technology, source_subscriber_no= acc_perm_packet.source_subscriber_no)
            print(acc_permited_packet)
            sock.sendto(acc_permited_packet.to_bytes(), addr)
        elif(res == "Not_Paid"):
            sub_not_paid_packet = SUBSCRIBER_NOT_PAID_PACKET(client_id = acc_perm_packet.client_id, segment_id = acc_perm_packet.segment_id, total_len = 1, technology = acc_perm_packet.technology, source_subscriber_no= acc_perm_packet.source_subscriber_no)
            print(sub_not_paid_packet)
            sock.sendto(sub_not_paid_packet.to_bytes(), addr)
        elif(res == "Tech_Mismatch"):
            sub_not_paid_packet = SUBSCRIBER_DOESNOT_EXIST_PACKET(client_id = acc_perm_packet.client_id, segment_id = acc_perm_packet.segment_id, total_len = 1, technology = acc_perm_packet.technology, source_subscriber_no= acc_perm_packet.source_subscriber_no)
            print(sub_not_paid_packet)
            sock.sendto(sub_not_paid_packet.to_bytes(), addr)
        else:
            sub_not_ex_packet = SUBSCRIBER_DOESNOT_EXIST_PACKET(client_id = acc_perm_packet.client_id, segment_id = acc_perm_packet.segment_id, total_len = 1, technology = acc_perm_packet.technology, source_subscriber_no= acc_perm_packet.source_subscriber_no)
            print(sub_not_ex_packet)
            sock.sendto(sub_not_ex_packet.to_bytes(), addr)
    except Exception as e:
        print("An exception occurred:", e)
        traceback.print_stack()