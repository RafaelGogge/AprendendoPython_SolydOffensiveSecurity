# Aula 5 - Estruturas de laço (WHILE e FOR)

nomes = ['Guilherme', 'Marcelo', 'Joao', 'Julia']

for nome in nomes: # "nome" pode ser substituido por qualquer valor, exemplo: X, Y, Z
    print(nome)

lista_de_numeros = range(0,10,2)
for item in lista_de_numeros:
    print(item)
#range cria uma lista com números, basta informar a quantidade, (0,10,2) de zero a 10 pulando 2 em 2

for i in range(4): # substitui o i por cada nome dentro da lista de acordo com o range de números
    print(nomes[i]) # para não dar erro, utilizar o len, veja abaixo:

for i in range(len(nomes)): # o len verá a quantia do range corretamente sem precisar expecificar 
    print(nomes[i])
    nomes.append('OII MONOIT') # para cada nome na lista será adicionado um OII

print(nomes)


palavra = 'Rafael Vieira'
for letra in palavra:
    print(letra) # printar cada letra em uma linha individualmente


i = 0
while i < 10:
    print('i ainda é menor que 10: ', i)
    i = i + 1

print('Acabou o while: ', i)

i = 0
while i < 20:
    i += 1 # mesma coisa do i++ do portugol
    print(i)


numero = 0
while True:
    print(numero)
    if numero == 20:
        break
    numero += 1
print('Saiu do while.')

