class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostrar_no(self):
        print(self.valor)


class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def inserirInicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def listaVazia(self):
        return self.primeiro is None

    def mostrarLista(self):
        if self.listaVazia():
            print('A lista está vazia')
            return None
        atual = self.primeiro
        while atual is not None:
            atual.valor.mostrarDetalhes()
            atual = atual.proximo
        print("")

    def inserirFim(self, valor):
        novo = No(valor)
        if self.listaVazia():
            self.primeiro = novo
            return
        atual = self.primeiro
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo

    def excluirValor(self, valor):
        if self.listaVazia():
            print("A lista está vazia")
            return None
        if self.primeiro.valor == valor:
            self.primeiro = self.primeiro.proximo
            return
        anterior = self.primeiro
        atual = anterior.proximo
        while atual is not None:
            if atual.valor == valor:
                anterior.proximo = atual.proximo
                return
            anterior = atual
            atual = atual.proximo
        print("Este valor não está na lista")

    def pesquisar(self, valor):
        if self.listaVazia():
            print("A lista está vazia")
            return None
        atual = self.primeiro
        while atual is not None:
            if atual.valor == valor:
                print("Valor encontrado na lista")
                return atual
            atual = atual.proximo
        print("valor não está na lista")
        return None

    def ordenar(self):
        if self.listaVazia():
            return
        trocado = True
        while trocado:
            trocado = False
            atual = self.primeiro
            while atual.proximo is not None:
                if atual.valor.ano > atual.proximo.valor.ano:
                    atual.valor, atual.proximo.valor = atual.proximo.valor, atual.valor
                    trocado = True
                atual = atual.proximo


class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrarDetalhes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

    def adicionarNaLista(self, lista):
        lista.inserirInicio(self)

    def removerDaLista(self, lista):
        lista.excluirValor(self)

    def pesquisarNaLista(self, lista):
        lista.pesquisar(self)

    def ordenarLista(self, lista):
        lista.ordenar()


carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Honda", "Civic", 2019)
carro3 = Carro("Ford", "Fusion", 2018)

lista = ListaEncadeada()

carro1.adicionarNaLista(lista)
carro2.adicionarNaLista(lista)
carro3.adicionarNaLista(lista)

carro1.removerDaLista(lista)

carro3.pesquisarNaLista(lista)

lista.ordenar()

lista.mostrarLista()