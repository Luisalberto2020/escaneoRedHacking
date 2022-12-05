from colorama import Fore, Back, Style
from concurrent.futures import ThreadPoolExecutor

from utils.network import Network
from utils.ping import Ping
from utils.portScanner import PortScanner


class AppService():

    @staticmethod
    def __make_ping(host: str,verbose:bool) -> dict:
        '''Realiza un ping a una ip'''
        result: dict = None
        if verbose:
            print(f'Pinging {host}')
        ping = Ping(host)
        if ping.is_alive():
            result = ping.get_sumary()

        return result


    @staticmethod
    def __make_ping_thread(hosts: list,threads:int,verbose:bool) -> list:
        '''Realiza un ping a una lista de ips'''
        results: list = []
        with ThreadPoolExecutor(max_workers=threads) as executor:
            for result in executor.map(AppService.__make_ping, hosts, [verbose] * len(hosts)):
                if result is not None:
                    results.append(result)

        return results

    @staticmethod
    def main_ping(args: dict) -> dict:
        '''Funcion principal del programa devuelve los resultados'''

        hosts:list = []
        result:list = []

        if args['red'] is not None:
            hosts = Network.get_hosts(args['red'])
        else:
            hosts.append(args['ip'])


        if not args['ping_null']:
            if args['threads'] == 1:
                for host in hosts:
                    i = AppService.__make_ping(host,args['verbose'])
                    if i is not None:
                        result.append(i)
            else:
                result = AppService.__make_ping_thread(hosts,args['threads'],args['verbose'])
        
        else:
            for host in hosts:
                result.append({'ip': host, 'sistema': 'Desconocido'})

        return result


    @staticmethod
    def __make_scan(host: str, ports: list,verbose:bool) -> list:
        '''Realiza un escaneo a un host'''
        result: list = []
        if verbose:
            print(f'{Back.YELLOW} Escanendo los puertos {ports} en {host} {Style.RESET_ALL}')

        for port in ports:
            scanner = PortScanner(host, port)
            if scanner.is_open():
                result.append(scanner.get_sumary())

        return result

    @staticmethod
    def main_scan(args: dict,hosts:list) -> dict:
        '''Funcion principal del programa devuelve los resultados'''

        ports:list = Network.get_ports(args['puerto'])
        if args['threads'] == 1:
            for host in hosts:
                    scan_port = AppService.__make_scan(host,ports,args['verbose'])

        else:
            for host in hosts:
                scan_port = AppService.__make_scan_thread(host,ports,args['threads'],args['verbose'])
