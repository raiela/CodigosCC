class Fila:
    def __init__(self, tam):
        self.tam = tam+1
        self.ini = 0
        self.fim = 0
        self.valor = [None]*self.tam

    def vazia(self):
        return self.ini == self.fim

    def cheia(self):
        return (self.fim+1)%self.tam == self.ini

    def enfileirar(self, valor):
        if not self.cheia():
            self.valor[self.fim] = valor
            self.fim = (self.fim+1)%self.tam
        else:
            print("Operação inválida")
            return "Fila cheia!"

    def desenfileirar(self):
        if not self.vazia():
            item = self.valor[self.ini]
            self.ini = (self.ini+1)%self.tam
            return item
        else:
            print("Operação inválida")
            return "Fila vazia"

    def imprimir(self):
        i = self.ini
        while i != self.fim:
            print(self.valor[i])
            i = (i+1)%self.tam

fila = Fila(10)