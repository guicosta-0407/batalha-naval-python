from jogador import Jogador
from computador import Computador


def jogar_partida(modo):

    j1 = Jogador("Jogador 1")
    if modo == 1:
        j2 = Computador("Computador")
    else:
        j2 = Jogador("Jogador 2")

    j1.tabuleiro.posicionar_frota()
    j2.tabuleiro.posicionar_frota()

    atual, outro = j1, j2

    while True:
        print(f"\n--- Vez de {atual.nome} ---")
        print(outro.tabuleiro.como_texto(False))

        linha, coluna = atual.escolher_jogada(outro)
        resultado, navio = outro.tabuleiro.receber_tiro(linha, coluna)
        atual.tiros_dados.add((linha, coluna))

        print(f"{atual.nome} jogou e o resultado foi: {resultado}")

        if outro.tabuleiro.todos_afundados():
            print(f"\n{atual.nome} venceu!")
            break

        if resultado == "agua":
            atual, outro = outro, atual

if __name__ == "__main__":
    jogar_partida(1)