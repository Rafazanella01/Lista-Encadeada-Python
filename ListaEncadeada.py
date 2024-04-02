from No import No

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def inserirInicio(self, valor): # Método Implementado na aula
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def listaVazia(self): # Método Implementado na aula
        return self.primeiro is None

    def mostrarLista(self): # Método Implementado na aula
        if self.listaVazia():
            print('A lista está vazia')
            return None
        atual = self.primeiro
        while atual is not None:
            atual.valor.mostrarDetalhes()
            atual = atual.proximo

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
        print("O Carro não está na lista")

    def pesquisar(self, valor):
        if self.listaVazia():
            print("A lista está vazia")
            return None
        atual = self.primeiro
        while atual is not None:
            if atual.valor == valor:
                print("Carro encontrado na lista")
                return atual
            atual = atual.proximo
        print("O Carro não está na lista")
        return None

    def ordenar(self):
        if self.lista_vazia():
         print("A lista está vazia!")
         return None                        # Nada a ordenar

        troca = True                          #a variavel troca serve para testar todos números da lista, quando nao tiver mais nenhum item para trocar ele para o loop
        while troca:
         troca = False
         anterior = None                     #inicializa uma variavel anterior
         atual = self.primeiro               #atual é definido como primeiro da lista

        while atual.proximo is not None:    #enquando tiver itens na lista
            proximo = atual.proximo           #inicializa a variavel proximo

            if atual.valor.ano > proximo.valor.ano:   #testa se o valor do 1º é maior que o 2º
                troca = True

            if anterior:                    #testa se já há algum item na variavel anterior
                anterior.proximo = proximo

            else:
                self.primeiro = proximo      #caso nao tenha um anterior, quer dizer que é o primeiro item a ser testado, logo é o primeiro da lista
            atual.proximo = proximo.proximo #atual aponta para o nó que o proximo está apontando
            proximo.proximo = atual         #proximo aponta para o nó que está como atual
            anterior = proximo              #o nó que está como proximo é atribuido a variavel anterior

        else:
             anterior = atual
             atual = atual.proximo
