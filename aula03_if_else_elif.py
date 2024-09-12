# Aula 3 - Operadores lógicos e estruturas de decisões IF, ELSE e ELIF

print('Selecione o nome de seu personagem: \n Opção 1: Joao\n Opção 2: Guilherme\n Opção 3: Maria')

opcao = input('Escolha uma opção: ')

if opcao == '1':
    print('O nome de seu personagem é: Joao')
elif opcao == '2':
    print('O nome de seu personagem é: Guilherme')
elif opcao == '3':
    print('O nome de sua personagem é: Maria')
else:
    print('Opção inválida')
