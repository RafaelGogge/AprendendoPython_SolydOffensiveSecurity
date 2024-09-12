#Buscando emails em sites
import re
import requests

requisicao = requests.get('https://unisales.br/contato/')
padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text)
if padrao:
    print(padrao)
else:
    print('Nenhum email localizado nesse site')