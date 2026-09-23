TAMANHO_TABULEIRO = 10
COLUNAS = "ABCDEFGHIJ"
AGUA, NAVIO, ACERTO, AGUA_ACERTADA = "~", "N", "X", "O"
TAMANHO_FROTA = {"grande":2, "pequeno": 3}
TAMANHO_NAVIO = {"pequeno": 2, "grande": 4}

def converter_coordenada(coordenada):
    coordenada = coordenada.strip().upper()

    if len(coordenada) < 2 or not coordenada[1:].isdigit(): #if para rejeitar as coordenadas invalidas
        raise ValueError("Formato invalido. Use letra + numero (ex.: C5).")
    
    letra_linha = coordenada[0]
    str_coluna = coordenada[1:]
    linha = ord(letra_linha) - ord('A')
    coluna = int(str_coluna) - 1

    if not (0 <= coluna < TAMANHO_TABULEIRO and 0 <= linha < TAMANHO_TABULEIRO): #if para verificar os valores que passaram cabem no tabuleiro (ex.: C11)
        raise ValueError("Fora do tabuleiro. Colunas A-J, linhas 1-10.")

    return linha, coluna