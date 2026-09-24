class Navio:
    def __init__(self, tipo, posicoes):
        self.tipo = tipo
        self.posicoes = posicoes
        self.atingidas = set()

    def registrar_tiro(self, posicao):
        if posicao in self.posicoes:
            self.atingidas.add(posicao)
            return True
        return False

    def esta_afundado(self):
        return len(self.atingidas) == len(self.posicoes)