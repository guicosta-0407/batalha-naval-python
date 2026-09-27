from utils import DIR_DATA, carregar_json, salvar_json

CAMINHO_ESTATISTICAS = DIR_DATA / "estatisticas.json"

PADRAO = {"partidas": 0, "vitorias": 0, "tiros": 0, "acertos": 0}

def registrar_partida(venceu, tiros, acertos):

    dados = carregar_json(CAMINHO_ESTATISTICAS, PADRAO.copy())

    dados["partidas"] += 1
    dados["tiros"] += tiros
    dados["acertos"] += acertos
    if venceu:
        dados["vitorias"] += 1

    salvar_json(CAMINHO_ESTATISTICAS, dados)

def calcular_aproveitamento(acertos, tiros):

    if tiros == 0:
        return 0.0
    return (acertos / tiros) * 100


def exibir():

    dados = carregar_json(CAMINHO_ESTATISTICAS, PADRAO.copy())
    aproveitamento = calcular_aproveitamento(dados["acertos"], dados["tiros"])

    print("=" * 50)
    print("ESTATISTICAS")
    print("=" * 50)
    print(f"Partidas jogadas: {dados['partidas']}")
    print(f"Vitorias: {dados['vitorias']}")
    print(f"Tiros dados: {dados['tiros']}")
    print(f"Acertos: {dados['acertos']}")
    print(f"Aproveitamento: {aproveitamento:.1f}%")