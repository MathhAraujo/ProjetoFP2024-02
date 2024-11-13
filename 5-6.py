import os
os.system("cls")

def arquivoHandler(openingFormat):
    try:
        arquivo = open("5-6.txt", openingFormat)
    except FileNotFoundError:
        open("5-6.txt", "x").close()
        arquivo = arquivoHandler(openingFormat)

    return arquivo

def addObjetivo(objetivo, valor):
    arquivo = arquivoHandler("a")

    arquivo.write(f"{objetivo}/{valor}\n")

    arquivo.close();