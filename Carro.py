class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrarDetalhes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")