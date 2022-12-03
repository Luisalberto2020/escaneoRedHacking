from concurrent.futures import ThreadPoolExecutor
from utils.network import Network
from utils.ping import Ping


class ArgumetosService():

    @staticmethod
    def __make_ping(host: str) -> dict:
        '''Realiza un ping a una ip'''
        result: dict = None
        ping = Ping(host)
        if ping.is_alive():
            result = ping.get_sumary()


        return result


    @staticmethod
    def main(args: dict) -> dict:
        '''Funcion principal del programa devuelve los resultados'''

        hosts:list = []
        active_hosts:list = []
        result:dict = {}

        if args['red'] is not None:
            hosts = Network.get_hosts(args['red'])
        else:
            hosts.append(args['ip'])


        if not args['ping_null']:
            if args['threads'] == 1:
                for host in hosts:
                    result += ArgumetosService.__make_ping(host)
            else:
                with ThreadPoolExecutor(max_workers=args['threads']) as executor:
                    for host in hosts:
                        executor.submit(ArgumetosService.__make_ping(host))
                    
                    
        else:
            active_hosts = hosts


        return result
            
            
            
