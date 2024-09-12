nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: ')) # int usado para números inteiros
altura = float(input('Digite sua altura: ')) # float usado para números quebrados
peso = float(input('Digite seu peso: ')) # float usado para números quebrados

if idade >= 18 and altura >= 1.70 and peso >= 60:
    print('Você está apto a entrar no exército!')
else:
    print('Você não está apto a entrar no exército!')