#Aula 11 - Tratamentos de erros e exceções (TRY e EXCEPT)

import time

def abre_arquivo():
    try:
        arquivo = open('arquivo.txt')
        return arquivo
    except Exception as erro:
        print('Erro, arquivo não existente', erro)
        return False
while not abre_arquivo():
    print('Tentando abrir o arquivo')

