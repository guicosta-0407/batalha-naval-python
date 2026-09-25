from utils import (
    TAMANHO_TABULEIRO, COLUNAS, AGUA, NAVIO, ACERTO, AGUA_ACERTADA,
    TAMANHO_NAVIO, TAMANHO_FROTA, NAVIO_AFUNDADO
) #adicionando as constantes que eu tinha esquecido
from navios import Navio
import random

class Tabuleiro:

    def __init__(self):
        self.grade = [
            [AGUA for _ in range(TAMANHO_TABULEIRO)]
            for _ in range(TAMANHO_TABULEIRO)
        ]
        self.navios = []

    def pode_posicionar(self, posicoes):

        for linha, coluna in posicoes:
            if not (0 <= linha < TAMANHO_TABULEIRO
                    and 0 <= coluna < TAMANHO_TABULEIRO):
                return False
            if self.grade[linha][coluna] != AGUA:
                return False
        return True

    def posicionar_navio_aleatorio(self, tipo):
        tamanho = TAMANHO_NAVIO[tipo]

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

        for tipo, quantidade in TAMANHO_FROTA.items():
            for _ in range(quantidade):
                self.posicionar_navio_aleatorio(tipo)

    def ja_jogada(self, linha, coluna):

        return self.grade[linha][coluna] in (ACERTO, AGUA_ACERTADA)

    def receber_tiro(self, linha, coluna):

        for navio in self.navios:
            if navio.registrar_tiro((linha, coluna)):
                self.grade[linha][coluna] = ACERTO
                if navio.esta_afundado():
                    for pos_linha, pos_coluna in navio.posicoes:
                        self.grade[pos_linha][pos_coluna] = NAVIO_AFUNDADO
                    return "afundado", navio
                return "acerto", navio

        self.grade[linha][coluna] = AGUA_ACERTADA
        return "agua", None

    def todos_afundados(self):

        for navio in self.navios:
            if not navio.esta_afundado():
                return False
        return True

    def como_texto(self, mostrar_navios):

        linhas = ["   " + " ".join(COLUNAS)]

        for indice, linha in enumerate(self.grade):
            simbolos = []
            for celula in linha:
                if celula == NAVIO and not mostrar_navios:
                    simbolos.append(AGUA)
                else:
                    simbolos.append(celula)
            linhas.append(f"{indice + 1:2d} " + " ".join(simbolos))
        return "\n".join(linhas)