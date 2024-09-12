#Aula 14 - Expressões regulares, procurando por e-mails

import re # regular expression // expressao regular // regex // padrões

string_de_teste = 'O gato, a gata, os gatinhos, os gatoes'

padrao = re.search(r'gat\w*', string_de_teste) # RAW String, tira o poder dos caracteres, ex.: \n
print(padrao.group()) # group para imprimir o texto // findall buscar tudo


padrao2 = re.findall(r'[gat]+', string_de_teste)

if padrao:
    print(padrao)
else:
    print('Erro, padrao')

if padrao2:
    print(padrao2)
else:
    print('Erro, padrao2')