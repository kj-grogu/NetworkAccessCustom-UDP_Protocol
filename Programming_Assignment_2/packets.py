Technologies = {
    '2G':2,
    '3G':3,
    '4G':4,
    '5G':5
}

class ACCESS_PERMISSION_PACKET:
    START_OF_PACKET = b"\xff\xff"
    END_OF_PACKET = b"\xff\xff"
    client_id = -1
    segment_id = -1
    total_len = -1
    access_permission = 0XFFF8
    source_subscriber_no = -1
    technology = -1

    def __init__(self, client_id, segment_id, total_len, technology, source_subscriber_no):
        self.client_id = client_id
        self.access_permission = 0XFFF8
        self.segment_id = segment_id
        self.total_len = total_len
        self.technology = technology
        self.source_subscriber_no = source_subscriber_no

    def to_bytes(self):
        packet = self.START_OF_PACKET
        packet += bytes([self.client_id])
        packet += self.access_permission.to_bytes(2, byteorder='big')
        packet += bytes([self.segment_id])
        packet += bytes([self.total_len])
        packet += bytes([self.technology])
        packet += self.source_subscriber_no.to_bytes(5, byteorder='big')
        packet += self.END_OF_PACKET
        return packet

    @classmethod
    def from_bytes(cls, packet):
        print(packet)
        if packet[0:2] != cls.START_OF_PACKET:
            raise ValueError("Invalid start of packet")
        if packet[-2:] != cls.END_OF_PACKET:
            raise ValueError("Invalid end of packet")
        client_id = packet[2]
        access_permission = int.from_bytes(packet[3:5], byteorder='big')
        segment_id = packet[5]
        total_len = packet[6]
        technology = packet[7]
        source_subscriber_no = int.from_bytes(packet[8:-2], byteorder='big')

        return cls(client_id, segment_id, total_len, technology, source_subscriber_no)

    def __str__(self):
        return f"ACCESS_PERMISSION_PACKET(Client ID={self.client_id}, Access Permission:{hex(self.access_permission)}, Segment ID={self.segment_id}, Length={self.total_len}, Technology={self.technology}, Source Subscriber No={self.source_subscriber_no})"

class ACCESS_PERMITTED_PACKET:
    START_OF_PACKET = b"\xff\xff"
    END_OF_PACKET = b"\xff\xff"
    client_id = -1
    segment_id = -1
    total_len = -1
    access_permission = 0XFFFB
    source_subscriber_no = -1
    technology = -1

    def __init__(self, client_id, segment_id, total_len, technology, source_subscriber_no):
        self.client_id = client_id
        self.access_permission = 0XFFFB
        self.segment_id = segment_id
        self.total_len = total_len
        self.technology = technology
        self.source_subscriber_no = source_subscriber_no

    def to_bytes(self):
        packet = self.START_OF_PACKET
        packet += bytes([self.client_id])
        packet += self.access_permission.to_bytes(2, byteorder='big')
        packet += bytes([self.segment_id])
        packet += bytes([self.total_len])
        packet += bytes([self.technology])
        packet += self.source_subscriber_no.to_bytes(5, byteorder='big')
        packet += self.END_OF_PACKET
        return packet

    @classmethod
    def from_bytes(cls, packet):
        print(packet)
        if packet[0:2] != cls.START_OF_PACKET:
            raise ValueError("Invalid start of packet")
        if packet[-2:] != cls.END_OF_PACKET:
            raise ValueError("Invalid end of packet")
        client_id = packet[2]
        access_permission = int.from_bytes(packet[3:5], byteorder='big')
        segment_id = packet[5]
        total_len = packet[6]
        technology = packet[7]
        source_subscriber_no = int.from_bytes(packet[8:-2], byteorder='big')

        return cls(client_id, segment_id, total_len, technology, source_subscriber_no)

    def __str__(self):
        return f"ACCESS_PERMITTED_PACKET(Client ID={self.client_id}, Access Permission:{hex(self.access_permission)}, Segment ID={self.segment_id}, Length={self.total_len}, Technology={self.technology}, Source Subscriber No={self.source_subscriber_no})"

class SUBSCRIBER_DOESNOT_EXIST_PACKET:
    START_OF_PACKET = b"\xff\xff"
    END_OF_PACKET = b"\xff\xff"
    client_id = -1
    segment_id = -1
    total_len = -1
    access_permission = 0XFFFA
    source_subscriber_no = -1
    technology = -1

    def __init__(self, client_id, segment_id, total_len, technology, source_subscriber_no):
        self.client_id = client_id
        self.access_permission = 0XFFFA
        self.segment_id = segment_id
        self.total_len = total_len
        self.technology = technology
        self.source_subscriber_no = source_subscriber_no

    def to_bytes(self):
        packet = self.START_OF_PACKET
        packet += bytes([self.client_id])
        packet += self.access_permission.to_bytes(2, byteorder='big')
        packet += bytes([self.segment_id])
        packet += bytes([self.total_len])
        packet += bytes([self.technology])
        packet += self.source_subscriber_no.to_bytes(5, byteorder='big')
        packet += self.END_OF_PACKET
        return packet

    @classmethod
    def from_bytes(cls, packet):
        print(packet)
        if packet[0:2] != cls.START_OF_PACKET:
            raise ValueError("Invalid start of packet")
        if packet[-2:] != cls.END_OF_PACKET:
            raise ValueError("Invalid end of packet")
        client_id = packet[2]
        access_permission = int.from_bytes(packet[3:5], byteorder='big')
        segment_id = packet[5]
        total_len = packet[6]
        technology = packet[7]
        source_subscriber_no = int.from_bytes(packet[8:-2], byteorder='big')

        return cls(client_id, segment_id, total_len, technology, source_subscriber_no)

    def __str__(self):
        return f"SUBSCRIBER_DOESNOT_EXIST_PACKET(Client ID={self.client_id}, Access Permission:{hex(self.access_permission)}, Segment ID={self.segment_id}, Length={self.total_len}, Technology={self.technology}, Source Subscriber No={self.source_subscriber_no})"

class SUBSCRIBER_NOT_PAID_PACKET:
    START_OF_PACKET = b"\xff\xff"
    END_OF_PACKET = b"\xff\xff"
    client_id = -1
    segment_id = -1
    total_len = -1
    access_permission = 0XFFF9
    source_subscriber_no = -1
    technology = ""

    def __init__(self, client_id, segment_id, total_len, technology, source_subscriber_no):
        self.client_id = client_id
        self.access_permission = 0XFFF9
        self.segment_id = segment_id
        self.total_len = total_len
        self.technology = technology
        self.source_subscriber_no = source_subscriber_no

    def to_bytes(self):
        packet = self.START_OF_PACKET
        packet += bytes([self.client_id])
        packet += self.access_permission.to_bytes(2, byteorder='big')
        packet += bytes([self.segment_id])
        packet += bytes([self.total_len])
        packet += bytes([self.technology])
        packet += self.source_subscriber_no.to_bytes(5, byteorder='big')
        packet += self.END_OF_PACKET
        return packet

    @classmethod
    def from_bytes(cls, packet):
        print(packet)
        if packet[0:2] != cls.START_OF_PACKET:
            raise ValueError("Invalid start of packet")
        if packet[-2:] != cls.END_OF_PACKET:
            raise ValueError("Invalid end of packet")
        client_id = packet[2]
        access_permission = int.from_bytes(packet[3:5], byteorder='big')
        segment_id = packet[5]
        total_len = packet[6]
        technology = packet[7]
        source_subscriber_no = int.from_bytes(packet[8:-2], byteorder='big')

        return cls(client_id, segment_id, total_len, technology, source_subscriber_no)

    def __str__(self):
        return f"SUBSCRIBER_NOT_PAID_PACKET(Client ID={self.client_id}, Access Permission:{hex(self.access_permission)}, Segment ID={self.segment_id}, Length={self.total_len}, Technology={self.technology}, Source Subscriber No={self.source_subscriber_no})"