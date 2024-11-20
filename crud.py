import os
os.system('cls')
import time as tempo

os.system("cls")

def arquivoHandler(nomeArquivo, openingFormat):
    try:
        arquivo = open(nomeArquivo, openingFormat)
    except FileNotFoundError:
        open(nomeArquivo, "x").close()
        arquivo = arquivoHandler(nomeArquivo, openingFormat)

    return arquivo

##1, 2 e 4 ---------------------------------------

def menu():
    print("Menu:")
    print("1. Adicionar Treino ou Competição")
    print("2. Visualizar Treinos ou Competição")
    print("3. Atualizar Treino ou Competição")
    print("4. Excluir Treino ou Competição")
    print("5. Sair")

def main():
    while True:
        menu()
        opcao = input("\nEscolha uma opção: ")
        if opcao == '1':
            print()
            adicionar_treino()
        elif opcao == '2':
            print()
            visualizar_treinos()
        elif opcao == '3':
            print()
            atualizar_treino()
        elif opcao == '4':
            print()
            excluir_treino()
        elif opcao == '5':
            print()
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def adicionar_treino():
    arquivo = arquivoHandler("treinos.txt", "a")

    data = verificaTreino()


    arquivo.write(data)


    print("\nTreino adicionado com sucesso!\n")

    arquivo.close()

def verificaTreino():
    tipoValido = ["Treino", "Competicao"]

    try:
        tipo = input("Você está salvando um treino ou competição?: ").lower().capitalize()

        if tipo not in tipoValido:
            raise ValueError
        
        data = input( "Qual a data(DD/MM/YYYY) em que ocorreu?: ")

        if len(data.split("/")) != 3:
            raise ValueError

        dist = float(input("Insira a distância percorrida(m)?:"))
        tempo = float(input("Qual a duração(minutos)?: "))

        local = input("Qual a localização em que ocorreu?: ")
        clima = input("Quais as condições climáticas?: ")

        return f"{tipo};{data};{dist};{tempo};{local};{clima}\n"
    
    except ValueError:
        print("Erro de tipagem")
        return verificaTreino()



def visualizar_treinos():
    arquivo = arquivoHandler("treinos.txt", "r")

    data = arquivo.readlines()

    if len(data) == 0:
        print("Não existem treinos ou competições salvas")
    else:
        for i in range(0, len(data)):
            current = data[i].split(";")

            print(f"{i + 1} -")
            print(f"Tipo: {current[0]}")
            print(f"Data: {current[1]}")
            print(f"Distância: {current[2]}")
            print(f"Tempo: {current[3]}")
            print(f"Local: {current[4]}")
            print(f"Clima: {current[5]}\n")

    arquivo.close()

def atualizar_treino():
    visualizar_treinos()
    
    try:
        index = int(input("Qual o dataset a modificar?: ")) - 1

        arquivo = arquivoHandler("treinos.txt", "r")
        data = arquivo.readlines()

        arquivo.close()

        data[index] = verificaTreino()

        arquivo = arquivoHandler("treinos.txt", "w")

        for i in data:
            arquivo.write(i)
        
        print("Dataset modificado com sucesso!")
        arquivo.close()

    except ValueError:
        print("Erro de tipagem")
    except IndexError:
        print("Dataset inexistente")

def excluir_treino():
    visualizar_treinos()

    try:
        index = int(input("Qual o dataset a apagar?: ")) - 1

        arquivo = arquivoHandler("treinos.txt", "r")
        data = arquivo.readlines()

        arquivo.close()

        arquivo = arquivoHandler("treinos.txt", "w")

        for i in range(len(data)):
            if i != index:
                arquivo.write(data[i])
        
        print("Dataset apagado com sucesso!\n")

        arquivo.close()

    except ValueError:
        print("Erro de tipagem")
    except IndexError:
        print("Dataset inexistente")


##3 ---------------------------------------

def filtrar_treinos():
    print("Filtrar Treinos")
    print("1. Filtrar por Distância")
    print("2. Filtrar por Tempo")
    escolha = input("Escolha uma opção (1 ou 2): ")
    
    if escolha == "1":
        try:
            distancia = float(input("Digite a distância desejada (km): "))
            filtrados = [treino for treino in treinos if treino["distancia"] == distancia]
            if filtrados:
                print(f"\nTreinos com {distancia} km:")
                for treino in filtrados:
                    print(treino)
            else:
                print("Nenhum treino encontrado com essa distância.")
        except ValueError:
            print("Por favor, digite um número válido para a distância.")
            
    elif escolha == "2":
        try:
            tempo = float(input("Digite o tempo máximo desejado (minutos): "))
            filtrados = [treino for treino in treinos if treino["tempo"] <= tempo]
            if filtrados:
                print(f"\nTreinos com tempo até {tempo} minutos:")
                for treino in filtrados:
                    print(treino)
            else:
                print("Nenhum treino encontrado com esse tempo.")
        except ValueError:
            print("Por favor, digite um número válido para o tempo.")
            
    else:
        print("Opção inválida. Por favor, selecione 1 ou 2.")

## 5 ---------------------------------------

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

## 7 -------------------------------
def funct_extra(t,x,decorrido,decorrido2):

    file = open('7.txt', 'a')

    t = tempo.asctime(tempo.localtime())
    t = t.split(" ")

    decorrido = t[3].split(":")

    input()

    x = tempo.asctime(tempo.localtime())
    x = x.split(" ")

    decorrido2 = x[3].split(":")

    print(f"Tempo de treino {int(decorrido2[2]) - int(decorrido[2])} foi de segundos")
    file.write(f"tempo de treino: {int(decorrido2[2]) - int(decorrido[2])} segundos\n")

    funct_extra(t,x,decorrido,decorrido2)

main()
    