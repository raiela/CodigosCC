class Pilha:
    def __init__(self, tam):
        self.tam = tam
        self.topo = 0
        self.valor = [None]*tam

    def vazia(self):
        return True if self.topo == 0 else False

    def cheia(self):
        return True if self.topo == self.tam else False

    def empilhar(self, valor):
        if not self.cheia():
            self.valor[self.topo] = valor
            self.topo += 1
        else:
            print("Pilha cheia")

    def desempilhar(self):
        if not self.vazia():
            self.topo -= 1
            item = self.valor[self.topo]
            return item
        else:
            print("Pilha vazia")

    def imprimir(self):
        while self.topo > 0:
            self.topo -= 1
            print(self.valor[self.topo])
