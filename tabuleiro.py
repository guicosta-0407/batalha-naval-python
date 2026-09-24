from utils import TAMANHO_TABULEIRO, AGUA,NAVIO, TAMANHOS, FROTA_PADRAO, ACERTO, TIRO_AGUA #adicionando as constantes que eu tinha esquecido
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

            posicoes = []
            for i in range(tamanho):
                if horizontal:
                    posicoes.append((linha, coluna + i))
                else:
                    posicoes.append((linha + i, coluna))

            if self.pode_posicionar(posicoes):
                navio = Navio(tipo, posicoes)
                self.navios.append(navio)
                for linha, coluna in posicoes:
                    self.grade[linha][coluna] = NAVIO
                return
    def posicionar_frota(self):
        for tipo, quantidade in FROTA_PADRAO.itens():
            for _ in range(quantidade):
                self.adicionar_navio_aleatorio(tipo)

    def ja_jogada(self, linha, coluna):
        return self.grade[linha][coluna] in (ACERTO, TIRO_AGUA)

    def receber_tiro(self, linha, coluna):
        for navio in self.navios:
            if navio.registrar_tiro((linha, coluna)):
                self.grade[linha][coluna] = ACERTO
                if navio.esta_afundado():
                    return "afundado", navio
                return "acerto", navio

        self.grade[linha][coluna] = TIRO_AGUA
        return "agua", None
                