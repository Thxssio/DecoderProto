from .SSLDetection import SSLDetection
from .SSLGeometry import SSLGeometry
from .SSLWrapper import SSLWrapper
from .UDPReceiver import UDPReceiver


class VisionProcessor:
    receiver: UDPReceiver = None
    wrapper: SSLWrapper = None
    detection: SSLDetection = None
    geometry: SSLGeometry = None

    def __init__(self, receiver, wrapper, detection, geometry):
        self.geometry = geometry
        self.receiver = receiver
        self.wrapper = wrapper
        self.detection = detection

    def process_vision(self):
        try:
            #print("Entrou no process_vision")
            data = self.receiver.receive()
            if data:
                #print("Recebeu pacote")                
                packet = self.wrapper.process_packet(data)
                if packet:
                    detection_frame = self.wrapper.process_detection(packet)
                    geometry_frame = self.wrapper.process_geometry(packet)
                    if detection_frame:
                        self.detection.process_positions(detection_frame)
                    if geometry_frame:
                        self.geometry.process_field_info(geometry_frame)
                    return self.set_vision_data()
                    
            else:
                print("Não recebeu data")
                return None
        except Exception as e:
            print(f"Erro ao processar visão: {e}")
            return None


        # print("Acabou")

    def set_vision_data(self):
        return {
            "robots_yellow": self.detection.robots_yellow,
            "robots_blue": self.detection.robots_blue,
            "ball_position": self.detection.ball_position,
            "field_size": self.geometry.field_size,
            "goal_size": self.geometry.goal_size,
        }