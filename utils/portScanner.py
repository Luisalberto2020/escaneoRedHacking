from scapy.all import IP, TCP, sr1,sr
import socket



''' 
    Flags for tcp packets
    'F': 'FIN',
    'S': 'SYN',
    'R': 'RST',
    'P': 'PSH',
    'A': 'ACK',
    'U': 'URG',
    'E': 'ECE',
    'C': 'CWR
    '''

class PortScanner():
    def __init__(self, host, port):
        '''Escanea un puerto de una maquina'''

        self.host = host
        self.port = port
        self.packet = IP(dst=self.host) / TCP(dport=self.port, flags='S')
        self.response = sr1(self.packet, timeout=0.5, verbose=0)
        


    def is_open(self) -> bool:
        '''Comprueba si el puerto esta abierto'''
        return self.response is not None and self.response[TCP].flags == 'SA'


    def get_host(self) -> str:
        return self.host


    def get_banner(self) -> str:
        '''Devuelve el banner del puerto'''
        try:
            servicio = socket.getservbyport(self.port)
        except:
            servicio = "¿?"
        
        
        return servicio

    def get_sumary(self,banner:bool) -> dict:
        '''Devuelve un diccionario con la informacion del puerto'''
        return {
            'servicio': self.get_banner() if banner else 'No disponible'
                }



    