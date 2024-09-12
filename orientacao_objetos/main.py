# Aula 9 - Orientação a objeto
from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo('rosa', 6, 'ford', 10)
print('Caminhão Rosa')
print('Cor: ', caminhao_rosa.cor)
print('Quantidade de rodas: ', caminhao_rosa.rodas)
print('Marca do veículo: ', caminhao_rosa.marca)
print('Capacidade do tanque de combustivel: ', caminhao_rosa.tanque)

print('')

carro_azul = Carro ('Azul', ' ', 'bmw', 30)
print('Carro Azul')
print('Cor: ', carro_azul.cor)
print('Quantidade de rodas: ', carro_azul.rodas)
print('Marca do veículo: ', carro_azul.marca)
print('Capacidade do tanque de combustivel: ', carro_azul.tanque)

carro_azul.abastecer(500)
print('Tanque', carro_azul.tanque)
