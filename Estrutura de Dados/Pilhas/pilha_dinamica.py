class Celula:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

class Pilha:
    def __init__(self):
        self.topo = None
        self.tam = 0

    def vazia(self):
        return True if self.tam == 0 else False

    def empilhar(self, valor):
        item = Celula(valor)
        item.prox = self.topo
        self.topo = item
        self.tam += 1

    def desempilhar(self):
        if not self.vazia():
            self.tam -= 1
            item = self.topo
            self.topo = item.prox
            return item.valor
        else:
            print("Pilha vazia")

    def imprimir(self):
        item = self.topo
        while item != None:
            print(item.valor)
            item = item.prox
        print("-----")