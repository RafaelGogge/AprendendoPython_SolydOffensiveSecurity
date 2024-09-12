# Aula 8 - Argumentos de linha de comando

import sys

argumentos = sys.argv #arg1 metodo, arg2 é o n1, arg3 é o n2

def soma(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mult(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1 / n2

if argumentos[1] == 'soma':
    resp = soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == 'sub':
    resp = sub(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == 'mult':
    resp = mult(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == 'div':
    resp = div(float(argumentos[2]), float(argumentos[3]))

print(resp)