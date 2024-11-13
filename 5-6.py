import os
os.system("cls")

def arquivoHandler(openingFormat):
    try:
        arquivo = open("5-6.txt", openingFormat)
    except FileNotFoundError:
        open("5-6.txt", "x").close()
        arquivo = arquivoHandler(openingFormat)

    return arquivo

def addObjetivo(objetivo, valor, medida):
    arquivo = arquivoHandler("a")

    arquivo.write(f"{objetivo}/{float(valor)}/{medida}\n")

    arquivo.close();

def atualizarObjetivo(objetivo, valorModificado):
    arquivo = arquivoHandler("r")

    objetivoLista = arquivo.readlines()

    if len(objetivoLista)== 0:
        print("Nenhum Objetivo registrado")
    else:
        newObjetivoList = []

        for i in objetivoLista:

            i = i.split("/")
            if i[0] == objetivo:
                i[1]= float(i[1])
                i[1] -= valorModificado

            newObjetivoList.append(f"{i[0]}/{i[1]}/{i[2]}")

    arquivo.close()
    
    arquivo = arquivoHandler("w")   
    
    for i in newObjetivoList:
        arquivo.write(f"{i}")
    
    arquivo.close()