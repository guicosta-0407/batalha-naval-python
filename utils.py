TAMANHO_TABULEIRO = 10
COLUNAS = "ABCDEFGHIJ"
AGUA, NAVIO, ACERTO, AGUA_ACERTADA, NAVIO_AFUNDADO = "~", "N", "X", "O", "#"
TAMANHO_FROTA = {"grande":2, "pequeno": 3}
TAMANHO_NAVIO = {"pequeno": 2, "grande": 4}

def converter_coordenada(coordenada):

    coordenada = coordenada.strip().upper()

    if len(coordenada) < 2 or not coordenada[1:].isdigit():
        raise ValueError("Formato invalido. Use letra + numero (ex.: C5).")

    letra_coluna = coordenada[0]
    str_linha = coordenada[1:]
    coluna = ord(letra_coluna) - ord('A')
    linha = int(str_linha) - 1

    if not (0 <= coluna < TAMANHO_TABULEIRO
            and 0 <= linha < TAMANHO_TABULEIRO):
        raise ValueError("Fora do tabuleiro. Colunas A-J, linhas 1-10.")

    return linha, coluna

def coordenada_para_texto(linha, coluna):
    return f"{chr(coluna + ord('A'))}{linha + 1}" #converte  (4,2) em D3

def formatar_tempo(segundos):
    segundos = int(segundos)
    minutos_totais, segundos_restantes = divmod(segundos, 60)
    horas, minutos_restantes = divmod(minutos_totais, 60)
    return f"{horas:02d}:{minutos_restantes:02d}:{segundos_restantes:02d}"