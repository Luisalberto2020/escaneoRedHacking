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
        result:list = [{'ip': '172.31.128.1', 'sistema': 'Linux'}]
        self.assertEqual(AppService.main_ping(argumentos),result)

    def test_No_Responding(self):

        argumentos:dict = {
            'red': None,
            'ip': '172.31.128.30',
            'puerto': '',
            'ping_null': False,
            'verbose': False,
            'threads': 1
        }
        result:list = []
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

        result:list = [{'ip': '172.31.128.1', 'sistema': 'Linux'}]
        result_funcion = AppService.main_ping(argumentos)
        print(result_funcion)

        self.assertEqual(result_funcion,result)


if __name__ == "__main__":
    unittest.main()