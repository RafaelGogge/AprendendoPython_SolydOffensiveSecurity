#Aula 11 - Tratamentos de erros e exceções (TRY e EXCEPT)

try: # tente fazer, se não der não trave o programa
    a = 120 / 0 # erro de divisão por zero
    ashdjadha() # erro de comando não existente
except Exception as erro: # define todos os erros e os salva no 'erro' para poder visualizar dps >print
    print('Houve um erro: ', erro)
print('Erro identificado')

