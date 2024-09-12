# Aula 2 - Variáveis, tipos, entrada, saída e operadores matemáticos

nome = 'Atumalaca'
idade = 22
altura = 1.51

print(nome)
print(idade)
print(altura)

print(type(nome)) # str - string
print(type(idade)) # int - inteiro
print(type(altura)) # float - float

print(nome, 'tem', idade, 'anos e possui',altura,'de altura ksksks.')

# aprendendo o comando input

nome = input('Escreva seu nome: ')
print('Prazer em lhe conhecer',nome)
idade = input('Qual sua idade? ')
print('Entendi, você tem', idade, 'anos.')
altura = input('Agora, preciso que me informe sua altura:')
print('Perfeito, você tem', altura, 'de altura.')