import time

from jogador import Jogador
from computador import Computador
from utils import coordenada_para_texto, formatar_tempo

def jogar_partida(modo):

    j1 = Jogador("Jogador 1")
    if modo == 1:
        j2 = Computador("Computador")
    else:
        j2 = Jogador("Jogador 2")

    j1.tabuleiro.posicionar_frota()
    j2.tabuleiro.posicionar_frota()

    atual, outro = j1, j2

    historico = []
    inicio = time.monotonic()

    while True:
        print(f"\n--- Vez de {atual.nome} ---")
        print(outro.tabuleiro.como_texto(False))

        linha, coluna = atual.escolher_jogada(outro)
        resultado, navio = outro.tabuleiro.receber_tiro(linha, coluna)
        historico.append({
            "jogador": atual.nome,
            "coord": coordenada_para_texto(linha, coluna),
            "resultado": resultado,
        })
        atual.tiros_dados.add((linha, coluna))

        if resultado == "agua":
            print("Água! Nenhum navio atingido nessa pocição.")
        elif resultado == "acerto":
            print("Acerto! Voce atingiu um navio inimigo.")
        else:
            print(f"Navio afundado! Você destruiu um navio {navio.tipo} do adversário.")

        if outro.tabuleiro.todos_afundados():
            print(f"\n{atual.nome} venceu!")
            duracao = time.monotonic() - inicio
            print(f"\n{'=' * 50}")
            print("FIM DE JOGO")
            print(f"{'=' * 50}")
            print(f"Vencedor: {atual.nome}")
            print(f"Total de jogadas: {len(historico)}")
            print(f"Tempo de partida: {formatar_tempo(duracao)}")
            break

        if resultado == "agua":
            atual, outro = outro, atual

if __name__ == "__main__":
    from menu import iniciar
    iniciar()