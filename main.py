import time

from jogador import Jogador
from computador import Computador
from utils import coordenada_para_texto, formatar_tempo, limpar_tela
from replay import salvar_partida
from estatisticas import registrar_partida

def jogar_partida(modo):

    nome_j1 = input("Digite o nome do Jogador 1: ").strip() or "Jogador 1"
    j1 = Jogador(nome_j1)

    if modo == 1:
        j2 = Computador("Computador")
    else:
        nome_j2 = input("Digite o nome do Jogador 2: ").strip() or "Jogador 2"
        j2 = Jogador(nome_j2)

    from menu import confirmar_posicionamento

    confirmar_posicionamento(j1)
    if modo == 2:
        limpar_tela()
        input(f"\nVez de {j2.nome} posicionar a frota. Pressione ENTER quando pronto...")
        limpar_tela()
        confirmar_posicionamento(j2)
    else:
        j2.tabuleiro.posicionar_frota()

    atual, outro = j1, j2

    historico = []
    inicio = time.monotonic()

    while True:

        if modo == 2:
            input(f"\nVez de {atual.nome}. Pressione ENTER quando estiver pronto (e o outro jogador nao estiver olhando)...")
            limpar_tela()
        print(f"\n--- Vez de {atual.nome} ---")
        if not isinstance(atual, Computador):
            mostrar_tabuleiros(atual, outro)

        linha, coluna = atual.escolher_jogada(outro)
        resultado, navio = outro.tabuleiro.receber_tiro(linha, coluna)
        historico.append({
            "jogador": atual.nome,
            "coord": coordenada_para_texto(linha, coluna),
            "resultado": resultado,
        })
        atual.tiros_dados.add((linha, coluna))
        if resultado != "agua":
            atual.acertos +=1

        if hasattr(atual, "registrar_resultado"):
            atual.registrar_resultado((linha, coluna), resultado)

        if resultado == "agua":
            print("Água! Nenhum navio atingido nessa pocição.")
        elif resultado == "acerto":
            print("Acerto! Voce atingiu um navio inimigo.")
        else:
            print(f"Navio afundado! Você destruiu um navio {navio.tipo} do adversário.")

        if outro.tabuleiro.todos_afundados():
            print(f"\n{atual.nome} venceu!")
            duracao = time.monotonic() - inicio
            salvar_partida(historico, atual.nome, duracao)
            registrar_partida(
                nome=atual.nome,
                venceu=True,
                tiros=len(atual.tiros_dados),
                acertos=atual.acertos,
            )
            print(f"\n{'=' * 50}")
            print("FIM DE JOGO")
            print(f"{'=' * 50}")
            print(f"Vencedor: {atual.nome}")
            print(f"Total de jogadas: {len(historico)}")
            print(f"Tempo de partida: {formatar_tempo(duracao)}")
            break

        if resultado == "agua":
            atual, outro = outro, atual

def mostrar_tabuleiros(jogador, adversario):
    
    linhas_proprio = jogador.tabuleiro.como_texto(True).split("\n")
    linhas_inimigo = adversario.tabuleiro.como_texto(False).split("\n")

    titulo_esquerda = f"SEU TABULEIRO ({jogador.nome})"
    titulo_direita = f"TABULEIRO INIMIGO ({adversario.nome})"
    print(f"\n{titulo_esquerda:<24}   {titulo_direita}")

    for linha_prop, linha_inim in zip(linhas_proprio, linhas_inimigo):
        print(f"{linha_prop:<24}   {linha_inim}")

if __name__ == "__main__":
    from menu import iniciar
    iniciar()