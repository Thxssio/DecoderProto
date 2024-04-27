from modules.UDPReceiver import UDPReceiver
from modules.SSLWrapper import SSLWrapper
from modules.SSLDetection import SSLDetection
from modules.SSLGeometry import SSLGeometry
from modules.VisionProcessor import VisionProcessor

def main():
    # Criar instâncias dos componentes necessários
    receiver = UDPReceiver()
    wrapper = SSLWrapper()
    detection = SSLDetection()
    geometry = SSLGeometry()

    # Criar uma instância do VisionProcessor
    vision_processor = VisionProcessor(receiver, wrapper, detection, geometry)

    # Iniciar o processamento de visão
    vision_data = vision_processor.process_vision()

    # Exibir ou realizar operações com os dados de visão, se necessário
    if vision_data:
        print("Dados de visão processados com sucesso:")
        print(vision_data)
    else:
        print("Falha ao processar os dados de visão.")

if __name__ == "__main__":
    main()
