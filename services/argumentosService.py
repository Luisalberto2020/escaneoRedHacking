from utils.network import Network
from utills.ping import Ping


class ArgumetosService():


    @staticmethod
    def make_all_ping(hosts:list) -> dict:
        '''Hace un ping a todos los hosts'''
        hosts_alive = {}
        for host in hosts:
            ping = Ping(host)
            if ping.is_alive():
                pass

        return hosts_alive

    @staticmethod
    def main(args: dict):
        '''Funcion principal'''

        hosts:list = []
        active_hosts:list = []

        if args['red'] is not None:
            hosts = Network.get_hosts(args['red'])
        else:
            hosts.append(args['ip'])


        if not args['ping_nul']:
            
