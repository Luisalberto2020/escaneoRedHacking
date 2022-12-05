import json

class AlmacenamientoService():

    @staticmethod
    def save_json(data_ping:dict,data_scan:dict,file:str):
        result:dict = {}
        for ip in data_ping:
            result[ip] = data_ping[ip]
            result[ip]['puertos'] = data_scan[ip]

        with open(file,'w') as f:
            f.write(json.dumps(result,indent=4))