from utils import DIR_DATA, carregar_json, salvar_json

CAMINHO_REPLAY = DIR_DATA / "ultima_partida.json"


def salvar_partida(historico, vencedor, duracao):

    dados = {
        "vencedor": vencedor,
        "duracao": duracao,
        "jogadas": historico,
    }
    salvar_json(CAMINHO_REPLAY, dados)

def reproduzir():

    dados = carregar_json(CAMINHO_REPLAY, None)

    if dados is None:
        print("Nenhuma partida foi jogada ainda.")
        return

    jogadas = dados["jogadas"]
    total = len(jogadas)

    print("Reproduzindo replay da última partida...\n")

    for indice, jogada in enumerate(jogadas, start=1):
        print(f"Jogada {indice:02d}/{total} - {jogada['jogador']} - {jogada['coord']} - {jogada['resultado']}")

        comando = input("[ENTER] Proxima jogada [Q] Sair do replay: ")
        if comando.strip().upper() == "Q":
            return

    print(f"\nFim do replay. Vencedor: {dados['vencedor']}")