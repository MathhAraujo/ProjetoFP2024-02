import os
os.system("cls")

def arquivoHandler(openingFormat):
    try:
        arquivo = open("5-6.txt", openingFormat)
    except FileNotFoundError:
        open("5-6.txt", "x")
        arquivo = arquivoHandler(openingFormat)

    return arquivo
