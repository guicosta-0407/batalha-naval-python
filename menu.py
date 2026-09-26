from main import jogar_partida
from tabuleiro import Tabuleiro
from utils import converter_coordenada


def exibir_menu_principal():

    print("=" * 50)
    print("BATALHA NAVAL - GPTECH GAMES")
    print("=" * 50)
    print("[1] Nova partida")
    print("[2] Ver estatisticas")
    print("[3] Assistir replay da ultima partida")
    print("[4] Creditos")
    print("[5] Sair")
    print("-" * 50)

    while True:
        opcao = input("Escolha uma opcao: ").strip()
        if opcao in ("1", "2", "3", "4", "5"):
            return opcao
        print("Opcao invalida. Tente novamente.")

def escolher_modo():

    print("Selecione o modo de jogo:")
    print("[1] Jogador vs Computador")
    print("[2] Dois Jogadores")
    print("[0] Voltar ao menu")

    while True:
        opcao = input(">> ").strip()
        if opcao in ("0", "1", "2"):
            return opcao
        print("Opcao invalida. Tente novamente.")

def iniciar():

    while True:
        opcao = exibir_menu_principal()

        if opcao == "1":
            modo = escolher_modo()
            if modo != "0":
                jogar_partida(int(modo))
        elif opcao == "2":
            pass
        elif opcao == "3":
            pass
        elif opcao == "4":
            print("\nDesenvolvido por Guilherme Marra - CEFET-MG\n")
        elif opcao == "5":
            print("Até a próxima!")
            break

def escolher_e_mover_navio(jogador):

    while True:
        texto = input("Numero do navio a mover: ").strip()
        total = len(jogador.tabuleiro.navios)
        if texto.isdigit() and 1 <= int(texto) <= total:
            navio = jogador.tabuleiro.navios[int(texto) - 1]
            break
        print("Numero invalido.")

    while True:
        texto = input("Nova coordenada inicial (ex.: C5): ")
        try:
            linha, coluna = converter_coordenada(texto)
        except ValueError as erro:
            print(erro)
            continue

        if jogador.tabuleiro.mover_navio(navio, linha, coluna):
            return
        print("Essa posicao nao cabe ou esta ocupada. Tente outra.")

def confirmar_posicionamento(jogador):

    jogador.tabuleiro.posicionar_frota()

    while True:
        print(f"\nFrota de {jogador.nome}:")
        print(jogador.tabuleiro.como_texto(True))
        for descricao in jogador.tabuleiro.listar_navios():
            print(descricao)

        print("[1] Confirmar  [2] Sortear tudo novamente  "
              "[3] Mover um navio")
        opcao = input(">> ").strip()

        if opcao == "1":
            return
        elif opcao == "2":
            jogador.tabuleiro = Tabuleiro()
            jogador.tabuleiro.posicionar_frota()
        elif opcao == "3":
            escolher_e_mover_navio(jogador)
        else:
            print("Opcao invalida.")