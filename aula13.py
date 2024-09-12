#Aula 13 - API, JSON e consultando listas de filmes // OMDB API - serve para filmes

import requests
import json

def requisicao(titulo):
    try:
        req = requests.get('https://www.omdbapi.com/?apikey=5727e934&=t' + titulo)
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro na requisição.')
        return None

try:
    def detalhes(filme):
        print('Título:', filme['Title'])
        print('Ano:', filme['Year'])
        print('Diretor:', filme['Director'])
        print('Atores:', filme['Actors'])
        print('Nota:', filme['imdbRating'])
        print('Capa:', filme['Poster'])
        print('')

except:
    print('Erro na requisição.')

sair = False
while not sair:
    op = input('Escreva o nome de um filme ou SAIR para fechar: ')
    if op == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        filme = requisicao(op)
        if filme ['Response'] == 'False':
            print('Seu filme não foi localizado.')
        else:
            detalhes(filme)
