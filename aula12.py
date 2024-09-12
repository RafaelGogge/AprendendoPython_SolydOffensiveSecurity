# Aula 12 - Bibliotecas, PIP e Requisições Web // serve para bruteforce

import requests

cabecalho = {'User agent':'Windows 13', 
            'Referer':'https://google.com', 
            'cf-ipcountry':'US'}

meus_cookies = {'Ultima visita': '10-10-2000'}

dados = {'username': 'anonymous_dark',
         'password':'we_are_legion'}

try:
    requisicao = requests.post('https://putsreq.com/mMYSq8eKWD4iCv32NKvV')
    headers = cabecalho
    cookies = meus_cookies
    data = dados
    print(requisicao.text)

except Exception as erro:
    print('Requisição deu erro', erro)
