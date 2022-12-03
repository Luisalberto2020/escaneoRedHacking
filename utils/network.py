class Network:
    '''Operaciones basicas con la red'''
    
    def __init__(self):
        pass
    
    
    @staticmethod
    def get_ip(network:str) -> str:
        
        
    
    
    @staticmethod
    def check_ip(ip: str) -> bool:
        return re.match(
            r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
            ip
        ) is not None
    
    
    @staticmethod
    def get_subnet(network: str) -> int:
        '''Obtiene las subred de una red' puede devolver una excepcion de format number exception'''
        
        
        pass 