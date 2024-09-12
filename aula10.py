# Aula 10 - Entrada e saída de arquivos

# w = modo de escrita com subscrita // r = modo de leitura // r+ modo escrita e leitura // a = append
# modo 'a' não apaga oq tem no arquivo // modo b = todos arquivos q n forem texto

arquivo = open('arquivo.txt', 'w')

for i in range (0,100):
    arquivo.write(str(i)+'\n') # a string 'str' precisa ser informada para escrever o arquivo // str, float, e demais
    