import unittest

from services.AppService import AppService


class SimplisticTest(unittest.TestCase):

    def test_pingBasico(self):

        argumentos:dict = {
            'red': None,
            'ip': '172.31.128.1',
            'puerto': '',
            'ping_null': False,
            'verbose': False,
            'threads': 1
        }
        result_ok:list = {'172.31.128.1': {'sistema': 'Linux', 'mac': '02:42:04:98:f8:5f'}}
        result = AppService.main_ping(argumentos)
        print(result)
        
        self.assertEqual(result,result_ok)

    def test_No_Responding(self):

        argumentos:dict = {
            'red': None,
            'ip': '172.31.128.30',
            'puerto': '',
            'ping_null': False,
            'verbose': False,
            'threads': 1
        }
        result:dict = {}
        self.assertEqual(AppService.main_ping(argumentos),result)

    def tes_pingRed(self):

        argumentos:dict = {
            'red': '172.31.128.0/24',
            'ip': None,
            'puerto': '',
            'ping_null': True,
            'verbose': False,
            'threads': 20
        }

        result:dict = [{'ip': '172.31.128.1', 'sistema': 'Linux'}]
        result_funcion = AppService.main_ping(argumentos)
        print(result_funcion)

        self.assertEqual(result_funcion,result)


    def test_scan_puertos(self):

        argumentos:dict = {
            'red': None,
            'ip': '172.31.128.1',
            'puerto': '1-100',
            'ping_null': True,
            'verbose': False,
            'threads': 20,
            'banner': True
        }
        result = AppService.main_scan(argumentos,['172.31.128.1'])
        print(result)
        result_ok:dict =  {'172.31.128.1': {}}
        
        self.assertEqual(result,result_ok)


    def test_scan_puertos2(self):
        '''Testea el escaneo de puertos'''

        argumentos:dict = {
            'red': None,
            'ip': None,
            'puerto': '1-100',
            'ping_null': True,
            'verbose': False,
            'threads': 20,
            'banner': True
        }
        result = AppService.main_scan(argumentos,['192.168.157.178','192.168.157.179'])
        print(result)
        result_ok:dict =  {'192.168.157.178': [{'servicio': 'ssh'}], '192.168.157.179': [{'servicio': 'ssh'}]}
        
        self.assertEqual(result,result_ok)


    def test_all(self):

        argumentos:dict = {
            'red': '192.168.157.0/24',
            'ip': None,
            'puerto': '1-100',
            'ping_null': True,
            'verbose': False,
            'threads': 20,
            'banner': True
        }
        result = AppService.main_ping(argumentos)
        result2 = AppService.main_scan(argumentos,result.keys())
        print(result2)

        result_ok:dict =  {'192.168.157.178': [{'servicio': 'ssh'}], '192.168.157.179': [{'servicio': 'ssh'}]}
        self.assertEqual(result2,result_ok)
        
        
        


if __name__ == "__main__":
    unittest.main()