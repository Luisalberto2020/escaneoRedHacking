from utils.menu import Menu
from colorama import Fore, Back, Style,init
from services.argumentosService import ArgumetosService

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


if __name__ == "__main__":
    init()
    try:
        menu = Menu()
        args = menu.get_args()
        ArgumetosService.main(args)
    except ValueError as error:
        print(f'{Fore.RED}Error: {error}{Style.RESET_ALL}')
        exit(1)
        
            
        
    
    
    