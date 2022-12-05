import logging

from colorama import Back, Fore, Style, init

from services.almacenamientoService import AlmacenamientoService
from services.AppService import AppService
from utils.menu import Menu

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


if __name__ == "__main__":
    init()
    try:
        menu = Menu()
        args = menu.get_args()
        if args['verbose']:
            print(Fore.GREEN + 'Iniciando Escaneo con ping'+ Style.RESET_ALL)

        result_ping:list = AppService.main_ping(args)
        #hosts:list = list(map(lambda x: x['ip'],result_ping))
        if args['verbose']:
            print(Fore.GREEN + 'Iniciando Escaneo de puertos'+ Style.RESET_ALL)

        result_ports:list = AppService.main_scan(args,result_ping.keys())

        menu.print_result(result_ping,result_ports)
        
        if  args['json']:
            AlmacenamientoService.save_json(result_ping,result_ports,args['json'])
            
            

    except ValueError  as error:
        print(f'{Fore.RED}Error: {error}{Style.RESET_ALL}')
        exit(1)
    except PermissionError as error:
        print(f'{Fore.RED} Por favor ejecuta el programa como administrador{Style.RESET_ALL}')
        exit(1)
