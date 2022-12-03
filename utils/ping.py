from scapy.all import IP, ICMP, sr1


class Ping():
    def __init__(self, target: str):
        self.target = target
        self.packet = IP(dst=self.target) / ICMP()
        self.response = sr1(self.packet, timeout=1,verbose=0)


    def is_alive(self) -> bool:
        return self.response is not None


    def get_system(self) -> str:
        system:str  = 'Desconocido'

        if self.is_alive():

            if self.response.ttl <= 64:
                system = 'Linux'

            elif self.response.ttl <= 128:
                system = 'Windows'

            elif self.response.ttl <= 255:
                system = 'Cisco'

            else:
                system = 'Desconocido'

        else:
            system = 'Apagado'

        return system


    def get_target(self) -> str:
        return self.target


    def get_sumary(self) -> dict:
        print(self.response)
        return {
            'ip': self.get_target(),
            'sistema': self.get_system(),
        }