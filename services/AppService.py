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
    def __make_ping_thread(hosts: list,threads:int,verbose:bool) -> dict:
        '''Realiza un ping a una lista de ips'''
        results: dict = {}
        with ThreadPoolExecutor(max_workers=threads) as executor:
            for result in executor.map(AppService.__make_ping, hosts, [verbose] * len(hosts)):
                if result is not None:
                    results[result['ip']] = result

        return results

    @staticmethod
    def main_ping(args: dict) -> dict:
        '''Funcion principal del programa devuelve los resultados'''

        hosts:list = []
        result:list = {}

        if args['red'] is not None:
            hosts = Network.get_hosts(args['red'])
        else:
            hosts.append(args['ip'])


        if not args['ping_null']:
            if args['threads'] == 1:
                for host in hosts:
                    i = AppService.__make_ping(host,args['verbose'])
                    if i is not None:
                        result[i.get('ip')] = {
                            'sistema': i.get('sistema'),
                            'mac': i.get('mac'),
                        }
            else:
                result = AppService.__make_ping_thread(hosts,args['threads'],args['verbose'])
        
        else:
            for host in hosts:
                result[i.get('ip')] = {'sistema': 'Desconocido', 'mac': 'Desconocido'}

        return result


    @staticmethod
    def __make_scan(host: str, ports: list,verbose:bool,banner:True) -> dict:
        '''Realiza un escaneo a un host'''
        result: dict = {}

        for port in ports:
            if verbose:
                print(f'Escaneando {host}:{port}')
            scanner = PortScanner(host, port)
            if scanner.is_open():
                result[port] = scanner.get_sumary(banner)

        return result


    @staticmethod
    def __make_port(host:str,port:int,verbose:bool,banner:True) -> dict:
        result:dict = None
        if verbose:
            print(f'Escaneado el puerto {port} de {host}')
        scan_port = PortScanner(host,port)
        if scan_port.is_open():
            result = scan_port.get_sumary(banner)
            result['port'] = port

        return result


    @staticmethod
    def __make_scan_thread(host: str, ports: list,verbose:bool,threads:int,banner:True) -> dict:
        '''Realiza un escaneo a un host'''
        result: dict = {}
        if verbose:
            print(f'{Fore.YELLOW} Escanendo los puertos {ports} en {host} {Style.RESET_ALL}')
            
        with ThreadPoolExecutor(max_workers=threads) as executor:
            for result_port in executor.map(AppService.__make_port, [host] * len(ports), ports, [verbose] * len(ports), [banner] * len(ports)):
                if result_port is not None:
                    result[result_port['port']] = {'servicio': result_port['servicio']}

        return result

    @staticmethod
    def main_scan(args: dict,hosts :list) -> dict:
        '''Funcion principal del programa devuelve los resultados'''
        result:dict = {}

        ports:list = Network.get_ports(args['puerto'])
        if args['threads'] == 1:
            for host in hosts:
                    if args['verbose']:
                        print(f'{Fore.YELLOW} Escanendo los puertos {ports} en {host} {Style.RESET_ALL}')
                    scan_port = AppService.__make_scan(host,ports,args['verbose'],args['threads'])
                    result[host] = scan_port

        else:
            for host in hosts:
                scan_port = AppService.__make_scan_thread(host,ports,args['verbose'],args['threads'],args['banner'])
                result[host] = scan_port

        return result
