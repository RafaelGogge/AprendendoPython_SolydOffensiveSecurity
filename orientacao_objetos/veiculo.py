# Aula 9 - Orientação a objeto
# classe é a receita do objeto, ela descreve o objeto
# objeto é a classe existente

class Veiculo:
    def __init__(self, cor, rodas, marca, tanque,):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque

    def abastecer(self, litros):
      self.tanque += litros
