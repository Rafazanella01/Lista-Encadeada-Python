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
            atual.mostrar_no()
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
                print(f"Valor {valor} encontrado na lista")
                return atual
            atual = atual.proximo
        print(f"valor {valor} não está na lista")
        return None

    def ordenar(self):
        if self.lista_vazia():
            return
        trocado = True
        while trocado:
            trocado = False
            atual = self.primeiro
            while atual.proximo is not None:
                if atual.valor > atual.proximo.valor:
                    atual.valor, atual.proximo.valor = atual.proximo.valor, atual.valor
                    trocado = True
                atual = atual.proximo


lista = ListaEncadeada()

for i in range(10):
    lista.inserir_inicio(i)

# inserir no fim
lista.inserir_fim(10)

# Excluindo valores
lista.excluir_valor(1)
lista.excluir_valor(2)
lista.excluir_valor(3)
lista.excluir_valor(0)
lista.excluir_valor(10)


# Pesquisando um valor
lista.pesquisar(10)

# Ordenando a lista
lista.ordenar()

# Mostrando a lista
lista.mostrar_lista()
