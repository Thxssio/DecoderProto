from .proto.ssl_vision_wrapper_pb2 import SSL_WrapperPacket

from jwt import DecodeError


class SSLWrapper:
    @staticmethod
    def process_packet(data):
        try:
            packet = SSL_WrapperPacket()
            packet.ParseFromString(data)
            return packet
        except DecodeError:
            print("DecodeError")
            return None

    @staticmethod
    def process_detection(packet):
        return packet.detection if packet.HasField("detection") else None

    @staticmethod
    def process_geometry(packet):
        return packet.geometry if packet.HasField("geometry") else None
