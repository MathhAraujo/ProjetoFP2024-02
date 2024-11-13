import os
import random
os.system("cls")

def arquivoHandler(nomeArquivo, openingFormat):
    try:
        arquivo = open(nomeArquivo, openingFormat)
    except FileNotFoundError:
        open(nomeArquivo, "x").close()
        arquivo = arquivoHandler(openingFormat)

    return arquivo

# 5 Start ---------------------------------------

def addObjetivo(objetivo, valor, medida):
    arquivo = arquivoHandler("5-6.txt","a")

    arquivo.write(f"{objetivo}/{float(valor)}/{medida}\n")

    arquivo.close();

def atualizarObjetivo(objetivo, valorModificado):
    arquivo = arquivoHandler("5-6.txt", "r")

    objetivoLista = arquivo.readlines()

    #Compara o objetivo com o passado e modifica apenas seu valor
    if len(objetivoLista)== 0:
        print("Nenhum Objetivo registrado")
    else:
        newObjetivoList = []

        for i in objetivoLista:

            i = i.split("/")
            if i[0] == objetivo:
                i[1]= float(i[1])
                i[1] -= valorModificado

            #Apaga objetivo e avisa ao usuário caso tenha sido concluido

            if float(i[1]) > 0:
                newObjetivoList.append(f"{i[0]}/{i[1]}/{i[2]}")
            else:
                print("Objetivo concluído!")

    arquivo.close()
    
    arquivo = arquivoHandler("5-6.txt", "w")   
    
    for i in newObjetivoList:
        arquivo.write(f"{i}")
    
    arquivo.close()

def deletaObjetivo(objetivo):
    arquivo = arquivoHandler("5-6.txt", "r")

    objetivoLista = arquivo.readlines()

    #Apaga todos os objetivos que encontrar com o nome passado

    if len(objetivoLista)== 0:
        print("Nenhum Objetivo registrado")
    else:
        newObjetivoList = []

        for i in objetivoLista:

            i = i.split("/")
            if i[0] != objetivo:
                newObjetivoList.append(f"{i[0]}/{i[1]}/{i[2]}")
                print("Objetivo deletado com sucesso!")

    arquivo.close()
    
    arquivo = arquivoHandler("5-6.txt", "w")   
    
    for i in newObjetivoList:
        arquivo.write(f"{i}")
    
    arquivo.close()

def printObjetivos():
    arquivo = arquivoHandler("5-6.txt", "r")

    arquivoList = arquivo.readlines()
    for i in arquivoList:
        i = i.split("/")
        print(f"{i[0]}: {i[1]} {i[2]}", end="")

# 5 End ---------------------------------------

# 6 Start ---------------------------------------

def sugereTreinos():
    arquivo = arquivoHandler("treinos.txt", "r")

    arquivoList = arquivo.readLines()
    lengArquivo = len(arquivoList)

    if lengArquivo > 0:
        # TODO: Trocar para formatação do txt treinos
        treinoEx = arquivoList[random.randint(0, lengArquivo)].split("/")
        
        #Sugere um treino aleatório com o objetivo de 10% a 50% maior
        treinoSugerido = f"treinoEx[0] + {float(treinoEx[1]) * random.uniform(1.1, 1.5)}"
        

    else:
        print("Nenhum treino para basear a sugestão")