import argparse
import re
from colorama import Fore, Back, Style


from .network import Network


class Menu:


    def  __init__(self):
        '''Crear el menu y parsea los argumentos'''
        parse = argparse.ArgumentParser(description='Herramienta de escaneo de puertos y de red')
        objetivos = parse.add_mutually_exclusive_group(required=True)
        objetivos.add_argument(
            '-r',
            '--red',
            help='Es la red a la que se debe escanear ejemplo 192.168.1.0/24',
            type=str,
        )

        objetivos.add_argument('-i',
            '--ip',
            help='Es la ip a la que se debe escanear ejemplo 192.168.0.15',
            type=str,
        )

        parse.add_argument('-p', '--puerto',
            help="""Es el puerto a escanear si no se pone nada o vacio no enscaneara puertos
                    si se pone all se escaneraran todos los puertos 
                    si se pone un rango de puertos se escanearan esos puertos ejemplo 1-1000
                    o si se especifica un puerto se escaneara ese puerto ejemplo 80
                    o si se pone varios puertos se escanearan esos puertos ejemplo 80,443,8080""",
            type=str,
            required=False,
            default=''
        )

        parse.add_argument(
            '-pn',
            '--ping-null',
            help='si se pone no se realizara un ping para comprobar si esta activo el equipo',
            action='store_true',
            default=False
        )

        parse.add_argument(
            '-v',
            '--verbose',
            help='Muestra mas informacion sobre el escaneo',
            action='store_true',
            required=False,
            default=False
        )

        parse.add_argument(
            '-t',
            '--threads',
            help='Numero de hilos para el escaneo',
            required=False,
            type=int,
            default=1
        )

        parse.add_argument(
            '-b',
            '--banner',
            help='Muestra el banner del puerto por defecto se muestra',
            action='store_true',
            default=True
        )

        parse.add_argument(
            '-j',
            '--json',
            help='Guarda los resultados en un archivo json por defecto no se guardaran',
            type=str,
            default=''
        )

        self.argumentos:dict = vars(parse.parse_args())
        self.__check_args()


    def __check_port(self)-> bool:
        """_summary_
            checkea los puertos si son validos
        Returns:
            bool: devuelve True si el puerto es valido el puerto
        """

        valid:bool = False
        
        if self.argumentos['puerto'] == '':
            valid = True
        elif self.argumentos['puerto'] == 'all':
            valid = True
        elif re.match(r'^\d+$', self.argumentos['puerto']):
            valid = True
        elif re.match(r'^\d+-\d+$', self.argumentos['puerto']):
            valid = True
        elif re.match(r'^\d+(,\d+)+$', self.argumentos['puerto']):
            valid = True

        return valid

    def __check_args(self):
        '''Comprueba que los arguemntos sean correctos'''
        if self.argumentos['verbose']:
            print(f'argumentos: {self.argumentos}')
        if self.argumentos['red'] is not None:
            if   not Network.check_network(self.argumentos['red']):
                raise ValueError('La red no es valida')

        if self.argumentos['ip'] is not None:
            if not Network.check_ip(self.argumentos['ip']):
                raise ValueError('La ip no es valida')
        if self.argumentos['threads'] < 1:
            raise ValueError('Los hilos no pueden ser menor que 1')

        if not self.__check_port():
            raise ValueError('El puerto no es valido')


    def get_args(self) -> dict:
        '''Devuelve los argumentos de la aplicacion'''
        return self.argumentos


    def print_result(self, result_ping:dict, result_ports:dict):
        '''Imprime el resultado del escaneo'''
        print(f'{Fore.GREEN}Escaneo de red{Style.RESET_ALL} \n \n')
        print(f'{Fore.BLUE}IP{Style.RESET_ALL} \t\t\t {Fore.BLUE}Sistema{Style.RESET_ALL}\t\t {Fore.BLUE}Mac{Style.RESET_ALL}')
        for ip in result_ping:
            print(f'{ip}  \t {result_ping[ip]["sistema"]} \t\t {result_ping[ip]["mac"]}')

        print(f'{Fore.BLUE}--------{Style.RESET_ALL} \t\t {Fore.BLUE}------{Style.RESET_ALL}\n')
        print(f'{Fore.GREEN}Escaneo de puertos{Style.RESET_ALL} \n ')
        print(f'{Fore.BLUE}IP{Style.RESET_ALL} \t\t\t {Fore.BLUE}Puerto{Style.RESET_ALL} \t {Fore.BLUE}Servicio{Style.RESET_ALL}')
        for ip in result_ports:
            for puerto in result_ports[ip]:
                print(f'{ip} \t {puerto} \t\t {result_ports[ip][puerto]["servicio"]}')
       