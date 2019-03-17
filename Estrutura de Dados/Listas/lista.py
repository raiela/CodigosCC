class Lista:
    def __init__(self, tam):
        self.tam = tam
        self.lista = [None]*self.tam
        self.fim = 0

    def vazia(self):
        return self.fim == 0

    def cheia(self):
        return self.fim == self.tam

    def adicionar(self, valor, pos):
        if not self.cheia() and pos <= self.fim:
            for i in range(self.fim, pos, -1):
                self.lista[i] = self.lista[i-1]
            self.lista[pos] = valor
            self.fim += 1
        else:
            print("Lista cheia!")
            return "Operação inválida!"

    def remover(self, pos):
        if not self.vazia() and self.fim >= pos:
            item = self.lista[pos]
            for i in range(pos, self.fim-1):
                self.lista[i] = self.lista[i+1]
            self.fim -= 1
            return item
        else:
            print("Erro!")
            return "Operação inválida!"

    def imprimir(self):
        print(self.lista)

    def imprimirSep(self):
        i = 0
        while i != self.fim:
            print(self.lista[i])
            i += 1


