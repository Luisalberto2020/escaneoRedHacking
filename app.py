from utils.menu import Menu
from colorama import Fore, Back, Style,init
from services.AppService import AppService

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


if __name__ == "__main__":
    init()
    try:
        menu = Menu()
        args = menu.get_args()
        if args['verbose']:
            print(Fore.GREEN + 'Iniciando Escaneo con ping'+ Style.RESET_ALL)

        result_ping:list = AppService.main_ping(args)
        print(result_ping)
        hosts:list = list(map(lambda x: x['ip'],result_ping))
        if args['verbose']:
            print(Fore.GREEN + 'Iniciando Escaneo de puertos'+ Style.RESET_ALL)

        result_ports:list = AppService.main_ports(args,hosts)

    except ValueError  as error:
        print(f'{Fore.RED}Error: {error}{Style.RESET_ALL}')
        exit(1)
    except PermissionError as error:
        print(f'{Fore.RED} Por favor ejecuta el programa como administrador{Style.RESET_ALL}')
        exit(1)
        
            
        
    
    
    