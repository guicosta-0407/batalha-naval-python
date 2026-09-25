from main import jogar_partida

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