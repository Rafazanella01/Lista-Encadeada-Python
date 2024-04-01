class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostrar_no(self):
        print(self.valor)


class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def inserir_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def lista_vazia(self):
        return self.primeiro is None

    def mostrar_lista(self):
        if self.lista_vazia():
            print('A lista está vazia')
            return None
        atual = self.primeiro
        while atual is not None:
            atual.valor.mostrar_detalhes()
            atual = atual.proximo
        print("")

    def inserir_fim(self, valor):
        novo = No(valor)
        if self.lista_vazia():
            self.primeiro = novo
            return
        atual = self.primeiro
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo

    def excluir_valor(self, valor):
        if self.lista_vazia():
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
        if self.lista_vazia():
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
        if self.lista_vazia():
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

    def mostrar_detalhes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

    def adicionar_a_lista(self, lista):
        lista.inserir_inicio(self)

    def remover_da_lista(self, lista):
        lista.excluir_valor(self)

    def pesquisar_na_lista(self, lista):
        lista.pesquisar(self)

    def ordenar_lista(self, lista):
        lista.ordenar()


carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Honda", "Civic", 2019)
carro3 = Carro("Ford", "Fusion", 2018)

lista = ListaEncadeada()

carro1.adicionar_a_lista(lista)
carro2.adicionar_a_lista(lista)
carro3.adicionar_a_lista(lista)

carro1.remover_da_lista(lista)

carro3.pesquisar_na_lista(lista)

lista.ordenar()

lista.mostrar_lista()