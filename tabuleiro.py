from utils import TAMANHO_TABULEIRO, AGUA
from navios import Navio
import random

class Tabuleiro:

    def __init__(self):
        self.grade = [[AGUA for _ in range(TAMANHO_TABULEIRO)] for _ in range(TAMANHO_TABULEIRO)]
        self.navios = []

    def pode_posicionar(self, posicoes):
        for linha, coluna in posicoes:
            if not (0 <= linha < TAMANHO_TABULEIRO and 0 <= coluna < TAMANHO_TABULEIRO):
                return False
            if self.grade[linha][coluna] != AGUA:
                return False
        return True

    def posicionar_navio_aleatorio(self, tipo):
        tamanho = TAMANHOS[tipo]

        while True:
            horizontal = random.choice([True, False])
            linha = random.randrange(TAMANHO_TABULEIRO)
            coluna = random.randrange(TAMANHO_TABULEIRO)

        for i in range(tamanho):
            if horizontal:
                posicoes.append((linha, coluna + i))
            else:
                posicoes.append((linha + i, coluna))

        if self.pode_posicionar(posicoes):