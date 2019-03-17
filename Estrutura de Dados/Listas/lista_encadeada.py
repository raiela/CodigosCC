class Celula:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

class Lista:
    def __init__(self):
        self.ini = Celula(None)
        self.fim = self.ini
        self.tam = 0

    def vazia(self):
        return True if self.tam == 0 else False

    def adicionar(self, valor, *pos):
        pos = pos[0] if pos != () else self.tam

        if pos <= self.tam:
            valorAnterior = self.ini
            item = Celula(valor)
            for i in range(pos):
                valorAnterior = valorAnterior.prox
            item.prox = valorAnterior.prox
            valorAnterior.prox = item
            self.tam += 1
        else:
            print("Erro!")
            return "Operação inválida!"

    def remover(self, *pos):
        pos = pos[0] if pos != () else self.tam-1
        if not self.vazia() and pos <= self.tam:
            anterior = self.ini
            for i in range(pos):
                anterior = anterior.prox
            aux = anterior.prox
            anterior.prox = aux.prox
            item = aux.valor
            self.tam -= 1
            del aux

            if self.tam == 0:
                self.fim = self.ini

            return item
        else:
            print("Erro")
            return "Operação Inválida"


    def imprimir(self):
        i = self.ini.prox
        while i != None:
            print(i.valor)
            i = i.prox

