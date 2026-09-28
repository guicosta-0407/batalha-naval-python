from utils import DIR_DATA, carregar_json, salvar_json

CAMINHO_ESTATISTICAS = DIR_DATA / "estatisticas.json"

PADRAO = {"partidas": 0, "vitorias": 0, "tiros": 0, "acertos": 0}

def registrar_partida(nome, venceu, tiros, acertos):

    dados = carregar_json(CAMINHO_ESTATISTICAS, {})
    stats = dados.get(nome, PADRAO.copy())

    stats["partidas"] += 1
    stats["tiros"] += tiros
    stats["acertos"] += acertos
    if venceu:
        stats["vitorias"] += 1

    dados[nome] = stats
    salvar_json(CAMINHO_ESTATISTICAS, dados)

def calcular_aproveitamento(acertos, tiros):

    if tiros == 0:
        return 0.0
    return (acertos / tiros) * 100


def exibir(nome):

    dados = carregar_json(CAMINHO_ESTATISTICAS, {})
    stats = dados.get(nome, PADRAO.copy())
    aproveitamento = calcular_aproveitamento(stats["acertos"], stats["tiros"])

    print("=" * 50)
    print(f"ESTATISTICAS - {nome}")
    print("=" * 50)
    print(f"Partidas jogadas: {stats['partidas']}")
    print(f"Vitorias: {stats['vitorias']}")
    print(f"Tiros dados: {stats['tiros']}")
    print(f"Acertos: {stats['acertos']}")
    print(f"Aproveitamento: {aproveitamento:.1f}%")

if __name__ == "__main__":
    # simula um jogador chamado "Gui" jogando 2 partidas
    registrar_partida("Gui", venceu=True, tiros=32, acertos=14)
    registrar_partida("Gui", venceu=False, tiros=27, acertos=11)

    # simula outro jogador com nome diferente
    registrar_partida("Maria", venceu=True, tiros=25, acertos=14)

    exibir("Gui")
    print()
    exibir("Maria")
    print()
    exibir("NomeQueNuncaJogou")   # deve vir tudo zerado, sem quebrar