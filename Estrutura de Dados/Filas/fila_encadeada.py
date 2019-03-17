class Celula:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

class Fila:
    def __init__(self):
        self.ini = None
        self.fim = None

    def vazia(self):
        return self.ini == None

    def enfileirar(self, valor):
        item = Celula(valor)
        if self.vazia():
            self.ini = item
        else:
            self.fim.prox = item
        self.fim = item

    def desenfileirar(self):
        if not self.vazia():
            valor = self.ini.valor
            self.ini = self.ini.prox
        else:
            print("Operação inválida")
            return "Fila vazia!!"

    def imprimir(self):
        item = self.ini
        while item != None:
            print(item.valor)
            item = item.prox
f = Fila()
