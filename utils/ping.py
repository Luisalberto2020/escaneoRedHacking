from scapy.all import IP, ICMP, sr1
from scapy.layers.l2 import getmacbyip


class Ping():
    def __init__(self, target: str):
        '''Hace un ping a una maquina y obtiene su sistema operativo'''
        self.target = target
        self.packet = IP(dst=self.target) / ICMP()
        self.response = sr1(self.packet, timeout=0.5,verbose=0)


    def is_alive(self) -> bool:
        '''Comprueba si la maquina esta encendida'''
        return self.response is not None


    def get_system(self) -> str:
        '''Obtiene el sistema operativo de la maquina'''
        system:str

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
        '''Obtiene la ip del objetivo'''
        return self.target


    def get_sumary(self) -> dict:
        '''Obtiene un resumen de la maquina despues de hacer el ping'''

        return {
            'ip': self.get_target(),
            'sistema': self.get_system(),
            'mac': getmacbyip(self.get_target())
        }