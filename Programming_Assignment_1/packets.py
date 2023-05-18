class ACK_PACKET:
    START_OF_PACKET = b"\xff\xff"
    TYPE_OF_PACKET = b"\xff\xf2"
    END_OF_PACKET = b"\xff\xff"
    client_id = -1
    segment_id = -1

    def __init__(self, client_id, segment_id):
        self.client_id = client_id
        self.segment_id = segment_id

    def to_bytes(self):
        packet = self.START_OF_PACKET
        packet += bytes([self.client_id])
        packet += self.TYPE_OF_PACKET
        packet += bytes([self.segment_id])
        packet += self.END_OF_PACKET
        return packet

    @classmethod
    def from_bytes(cls, packet):
        if packet[0:2] != cls.START_OF_PACKET:
            raise ValueError("Invalid start of packet")
        if packet[-2:] != cls.END_OF_PACKET:
            raise ValueError("Invalid end of packet")
        if packet[3:5] != cls.TYPE_OF_PACKET:
            raise ValueError("Invalid type of packet")
        client_id = packet[2]
        segment_id = packet[5]
        return cls(client_id, segment_id)

    def __str__(self):
        return f"ACK_PACKET(Client ID={self.client_id}, Type:{self.TYPE_OF_PACKET}, Segment ID={self.segment_id})"


class DATA_PACKET:
    START_OF_PACKET = b"\xff\xff"
    TYPE_OF_PACKET = b"\xff\xf1"
    END_OF_PACKET = b"\xff\xff"
    client_id = -1
    segment_id = -1
    total_len = -1
    payload = ""

    def __init__(self, client_id, segment_id, total_len, payload):
        self.client_id = client_id
        self.segment_id = segment_id
        self.total_len = total_len
        self.payload = payload

    def to_bytes(self):
        packet = self.START_OF_PACKET
        packet += bytes([self.client_id])
        packet += self.TYPE_OF_PACKET
        packet += bytes([self.segment_id])
        packet += bytes([self.total_len])
        packet += bytes(self.payload, encoding="utf-8")
        packet += self.END_OF_PACKET
        return packet

    @classmethod
    def from_bytes(cls, packet):
        print(packet)
        if packet[0:2] != cls.START_OF_PACKET:
            raise ValueError("Invalid start of packet")
        if packet[-2:] != cls.END_OF_PACKET:
            raise ValueError("Invalid end of packet")
        if packet[3:5] != cls.TYPE_OF_PACKET:
            raise ValueError("Invalid type of packet")
        client_id = packet[2]
        segment_id = packet[5]
        total_len = packet[6]
        payload = packet[7:-2].decode('utf-8')

        return cls(client_id, segment_id, total_len, payload)

    def __str__(self):
        return f"DATA_PACKET(Client ID={self.client_id}, Type:{self.TYPE_OF_PACKET}, Segment ID={self.segment_id}, Length={self.total_len}, Payload={self.payload})"


class REJECT_PACKET:
    START_OF_PACKET = b"\xff\xff"
    TYPE_OF_PACKET = b"\xff\xf3"
    END_OF_PACKET = b"\xff\xff"

    REJECT_CODE_OUT_OF_SEQUENCE = b"\xff\xf4"
    REJECT_CODE_LENGTH_MISMATCH = b"\xff\xf5"
    REJECT_CODE_END_OF_PACKET_MISSING = b"\xff\xf6"
    REJECT_CODE_DUPLICATE_PACKET = b"\xff\xf7"

    client_id = -1
    reject_code = -1
    segment_id = -1

    def __init__(self, client_id, segment_id, reject_code):
        self.client_id = client_id
        self.segment_id = segment_id
        self.reject_code = reject_code

    def to_bytes(self):
        packet = self.START_OF_PACKET
        packet += bytes([self.client_id])
        packet += self.TYPE_OF_PACKET
        packet += self.reject_code
        packet += bytes([self.segment_id])
        packet += self.END_OF_PACKET
        return packet

    @classmethod
    def from_bytes(cls, packet):
        if packet[0:2] != cls.START_OF_PACKET:
            raise ValueError("Invalid start of packet")
        if packet[-2:] != cls.END_OF_PACKET:
            raise ValueError("Invalid end of packet")
        if packet[3:5] != cls.TYPE_OF_PACKET:
            raise ValueError("Invalid type of packet")
        client_id = packet[2]
        segment_id = packet[7]
        reject_code = packet[5:7]
        return cls(client_id, segment_id, reject_code)

    def __str__(self):
        return f"REJECT_PACKET(Client ID={self.client_id}, Type:{self.TYPE_OF_PACKET}, Segment ID={self.segment_id}, Reject Code={'0X' + self.reject_code.hex()})"

# \\wsl.localhost\Ubuntu\home\zzubuntu\dev