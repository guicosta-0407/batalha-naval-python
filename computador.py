import random

from jogador import Jogador
from utils import TAMANHO_TABULEIRO


class Computador(Jogador):

    def __init__(self, nome):
        super().__init__(nome)
        self.alvos = []   # fila de posicoes a testar apos um acerto


    def escolher_jogada(self, adversario):

        while self.alvos:
            jogada = self.alvos.pop(0)
            if jogada not in self.tiros_dados:
                return jogada

        livres = [
            (linha, coluna)
            for linha in range(TAMANHO_TABULEIRO)
            for coluna in range(TAMANHO_TABULEIRO)
            if (linha, coluna) not in self.tiros_dados
        ]
        return random.choice(livres)

    def registrar_resultado(self, jogada, resultado):

        linha, coluna = jogada
        if resultado == "acerto":
            for vizinho in self._vizinhos(linha, coluna):
                if vizinho not in self.tiros_dados:
                    self.alvos.append(vizinho)
        elif resultado == "afundado":
            self.alvos.clear()

    def _vizinhos(self, linha, coluna):

        vizinhos = []
        for d_linha, d_coluna in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nova_linha, nova_coluna = linha + d_linha, coluna + d_coluna
            if (0 <= nova_linha < TAMANHO_TABULEIRO
                    and 0 <= nova_coluna < TAMANHO_TABULEIRO):
                vizinhos.append((nova_linha, nova_coluna))
        return vizinhos