from tabuleiro import Tabuleiro
from utils import converter_coordenada

class Jogador:

    def __init__(self, nome):
        self.nome = nome
        self.tabuleiro = Tabuleiro()
        self.tiros_dados = set()
        self.acertos = 0

    def escolher_jogada(self, adversario):
        while True:
            texto = input("Faça sua jogada (ex.: C5): ")
            try:
                linha, coluna = converter_coordenada(texto)
            except ValueError as erro:
                print(erro)
                continue

            if adversario.tabuleiro.ja_jogada(linha, coluna):
                print("Essa posição já foi jogada. Tente outra.")
                continue

            return linha, coluna