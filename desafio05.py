print('\n      * Controle Lista Convidados *')

numero_convidados = input('Números de Convidados: ')
lista = []

l = 1
while l <= int(numero_convidados):
    nome_convidado = input('Nome do Convidado(a) #' + str(l) + ': ')
    lista.append(nome_convidado)
    l += 1

print('Total de convidados: ', numero_convidados)

print('\nNome dos Convidados(as)')
for nome_convidado in lista:
    print(nome_convidado)
