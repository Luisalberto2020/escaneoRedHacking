import re

class Network:
    '''Operaciones basicas con la red'''

    def __init__(self):
        pass


    @staticmethod
    def check_ip(ip: str) -> bool:
        return re.match(
            r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
            ip
        ) is not None


    @staticmethod
    def get_ip(network:str) -> str:
        ip =  network.split('/')[0]
        if not  Network.check_ip(ip):
            raise ValueError('La ip no es valida')
        return ip


    @staticmethod
    def check_subnet(subnet: int) -> bool:
        return 0 < subnet < 32


    @staticmethod
    def get_subnet(network: str) -> int:
        '''Obtiene las subred de una red' puede devolver una excepcion de format number exception'''
        try:
            subnet = int(network.split('/')[1])
        except IndexError:
            raise ValueError('La subred no es valida')

        if not Network.check_subnet(subnet):
            raise ValueError('La subred no es valida')
        return subnet


    @staticmethod
    def check_network(network: str) -> bool:
        '''Comprueba que la red sea correcta'''
        exito:bool
        try:
            Network.get_ip(network)
            Network.get_subnet(network)
            exito =  True
        except ValueError:
            exito = False
        return exito


    @staticmethod
    def get_total_hosts(subnet: int) -> int:
        '''Calcula el numero de hosts que tiene una red'''
        return 2 ** (32 - subnet)


    @staticmethod
    def get_hosts(network:str) -> list:
        '''Obtiene los hosts de una red'''
        hosts:list = []
        initial_ip:str = Network.get_ip(network)
        subnet:int = Network.get_subnet(network)
        total_hosts:int = Network.get_total_hosts(subnet)
        host = initial_ip.split('.')
        acumulator = int(host[3])
        
        for i in range(total_hosts - 1):
            if  acumulator > 253:
                acumulator = 0
                host[3] = str(acumulator)
                host[2] = str(int(host[2]) + 1)
                if int(host[2]) > 253:
                    host[2] = '0'
                    host[1] = str(int(host[1]) + 1)
                    if int(host[1]) > 253:
                        host[1] = '0'
                        host[0] = str(int(host[0]) + 1)


                hosts.append('.'.join(host))
            else:
                acumulator += 1
                host[3] = str(acumulator)
                hosts.append('.'.join(host))


        return hosts


    @staticmethod
    def get_ports(ports:str) -> list:
        '''Obtiene los puertos de un string'''
        ports_list:list = []
        if ports == 'all':
            ports_list = list(range(1, 65536))
        elif re.match(r'^\d+$', ports):
            ports_list.append(int(ports))
        elif re.match(r'^\d+-\d+$', ports):
            ports_list = list(range(int(ports.split('-')[0]), int(ports.split('-')[1]) + 1))
        elif re.match(r'^\d+(,\d+)+$', ports):
            ports_list = [int(port) for port in ports.split(',')]

        return ports_list