from Carro import Carro
from ListaEncadeada import ListaEncadeada

carro1 = Carro("Volkswagen", "Fusca", 1977)
carro2 = Carro("Chevrolet", "Chevette", 1973)
carro3 = Carro("DMC", "DeLorean DMC 12", 1981)

lista = ListaEncadeada()

lista.inserirInicio(carro1)
lista.inserirInicio(carro2)
lista.inserirInicio(carro3)

#lista.excluirValor(carro1)

lista.pesquisar(carro2)

lista.ordenar()

lista.mostrarLista()
