import socket
import struct


class UDPReceiver:
    def __init__(self, ip="224.5.23.2", port=10006):
        self.ip = ip
        self.port = port
        self.sock = None
        self.max_size = 65536
        self.open()

    def open(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(("", self.port))
        group = socket.inet_aton(self.ip)
        mreq = struct.pack("4sL", group, socket.INADDR_ANY)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    def close(self):
        self.sock.close()

    def receive(self):
        try:
            #print("Entrou no receive")
            data, _ = self.sock.recvfrom(self.max_size)
            #print(data)
            return data
        except Exception as e:
            print("Exception: ", e)
            print("Erro ao receber pacote")
            return None