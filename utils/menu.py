import argparse


from .network import Network


class Menu:


    def  __init__(self):
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

        self.argumentos:dict = vars(parse.parse_args())
        self.__check_args()


    def __check_args(self):
        '''Comprueba que los arguemntos sean correctos'''
        print(self.argumentos)

        if  not ((self.argumentos['red'] is not None) and Network.check_network(self.argumentos['red'])):
            raise ValueError('La red no es valida')
        
        if self.argumentos['ip'] is not None:
            if not Network.check_ip(self.argumentos['ip']):
                raise ValueError('La ip no es valida')


    def get_args(self) -> dict:
        '''Devuelve los argumentos de la aplicacion'''
        return self.argumentos
