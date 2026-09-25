import random

from jogador import Jogador
from utils import TAMANHO_TABULEIRO


class Computador(Jogador):

    def escolher_jogada(self, adversario):

        livres = [
            (linha, coluna)
            for linha in range(TAMANHO_TABULEIRO)
            for coluna in range(TAMANHO_TABULEIRO)
            if (linha, coluna) not in self.tiros_dados
        ]
        return random.choice(livres)
