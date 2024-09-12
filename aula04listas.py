# Aula 4 - Strings e listas

frase = 'Oi, tudo bem?'
lista_nomes = ['Rafael', 'Manoela', 'Beatriz', 'Gabriel', 'Lucas', 'Joao']
lista_nomes.append('Alienigena') #append é usado para inserir itens na lista sempre na ultima posição
lista_nomes.remove('Alienigena') #remove é usado para remover itens da lista
lista_nomes.insert(1, 'Alienigena') #insert é usado para inserir um item na posição especifica
lista_nomes[6] = 'Alien' #substitui o item 6 - Joao por Alien

contador_rafael = lista_nomes.count('Rafael') #count conta quantas vezes o item se repete


print(frase[0:13])
print(frase[::-1]) # escrevendo frases invertidas

# Para pegar o ULTIMO item da lista sem saber o tamanho dela, utilize -1 (numeros negativos)

print(lista_nomes[0:8]) 
print(contador_rafael)
print(lista_nomes[-1:-9:-1]) #escrevendo a lista de modo inverso -1 começar do ultimo, -9 número de itens da lista, -1 modo inverso da lista de tras para frente


print(len(frase)) #len conta quantos itens possui dentro da lista 
print(len(lista_nomes)) #len conta quantos itens possui dentro da lista 

print(lista_nomes.pop()) #pop printa o ultimo item e o remove da lista
print(lista_nomes.pop())
print(lista_nomes.pop())
print(lista_nomes.pop())
print(lista_nomes.pop())
print(lista_nomes)