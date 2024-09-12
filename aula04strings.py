frase = 'Oi, Tudo Bem?'
lista_nomes = ['Rafael', 'Manoela', 'Beatriz', 'Gabriel', 'Lucas', 'Joao']

print(frase.lower()) #lower > transforma para minusculas apenas na hora do print, sem alterar a lista
print(frase.upper()) #upper > transforma para maiusculas apenas na hora do print, sem alterar a lista

frase_nova = frase + ' Como vai você?'
print(frase_nova)

frase_separada = frase.split(',') #split serve para transformar frases em listas separando no item que você pedir, no exemplo foi utilizado a virgula, ela não entrará na lista

print(frase_separada)
print(frase_separada[0])
print(frase_separada[1])
