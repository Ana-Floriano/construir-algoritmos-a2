from datetime import datetime, timedelta
import requests

def cotar():
    
    data_atual = datetime.now()
    resultado = []

    for i in range(365):
        dia = data_atual - timedelta(days=i)

        while True:
            data_str = dia.strftime("%m-%d-%Y")
            url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data_str}'&$top=100&$format=json"

            res = requests.get(url)
            res_json = res.json()

            if res_json.get("value"):
                resultado.append(res_json["value"][0]["cotacaoCompra"])
                break

            dia = dia - timedelta(days=1)

    return resultado

print(cotar())
