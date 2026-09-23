from utils import converter_coordenada

coordenada = input("Testando conversão: ")
linha, coluna = converter_coordenada(coordenada)

print(f"coordenada: {coordenada}")
print(f"linha: {linha}")
print(f"coluna: {coluna}")