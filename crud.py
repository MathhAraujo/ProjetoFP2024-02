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
    print("\nMenu:")
    print("1. Adicionar Treino ou Competição")
    print("2. Visualizar Treinos ou Competição")
    print("3. Atualizar Treino ou Competição")
    print("4. Filtrar Treino")
    print("5. Excluir Treino ou Competição")
    print("6. Contar tempo de treino")
    print("7. Abrir menu de Objetivos")
    print("8. Sugerir treino")
    print("9. Sair")

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
            filtrar_treinos()
        elif opcao == '5':
            print()
            excluir_treino()
        elif opcao == '6':
            print()
            funct_extra()
        elif opcao == '7':
            print()
            menuObjetivo()
        elif opcao == '8':
            print()
            sugereTreino()
        elif opcao == '9':
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
        tempo = int(input("Qual a duração(segundos)?: "))

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

def carregar_treinos_arquivo():
    treinos = []
    nome_arquivo = "treinos.txt"
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                partes = linha.strip().split(';')
                if len(partes) == 6: 
                    try:
                        tipo = partes[0].strip()
                        data = partes[1].strip()
                        distancia = float(partes[2].strip())
                        tempo = float(partes[3].strip())
                        localizacao = partes[4].strip()
                        clima = partes[5].strip()
                        treinos.append((tipo, data, distancia, tempo, localizacao, clima))
                    except ValueError:
                        print(f"Erro ao processar linha: {linha}. Certifique-se de que os dados numéricos são válidos.")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    return treinos

def filtrar_treinos():
    print("Filtrar Treinos")
    print("1. Filtrar por Distância")
    print("2. Filtrar por Tempo")
    escolha = input("Escolha uma opção (1 ou 2): ")
    
    treinos = carregar_treinos_arquivo()
    
    if not treinos:
        print("Nenhum treino carregado do arquivo.")
        return
    
    if escolha == "1":
        try:
            distancia = float(input("Digite a distância desejada (km): "))
            filtrados = [treino for treino in treinos if treino[2] == distancia]
            if filtrados:
                print(f"\nTreinos com {distancia} km:")
                for treino in filtrados:
                    print(f"Tipo: {treino[0]}, Data: {treino[1]}, Distância: {treino[2]} km, Tempo: {treino[3]} min, Localização: {treino[4]}, Clima: {treino[5]}")
            else:
                print("Nenhum treino encontrado com essa distância.")
        except ValueError:
            print("Por favor, digite um número válido para a distância.")
            
    elif escolha == "2":
        try:
            tempo = float(input("Digite o tempo máximo desejado (minutos): "))
            filtrados = [treino for treino in treinos if treino[3] <= tempo]
            if filtrados:
                print(f"\nTreinos com tempo de {tempo} minutos:")
                for treino in filtrados:
                    print(f"Tipo: {treino[0]}, Data: {treino[1]}, Distância: {treino[2]} km, Tempo: {treino[3]} min, Localização: {treino[4]}, Clima: {treino[5]}")
            else:
                print("Nenhum treino encontrado com esse tempo.")
        except ValueError:
            print("Por favor, digite um número válido para o tempo.")
            
    else:
        print("Opção inválida. Por favor, selecione 1 ou 2.")

## 5 ---------------------------------------

def menuObjetivo():
    print("Menu:")
    print("1. Exibir objetivos")
    print("2. Adicionar Objetivo")
    print("3. Atualizar Objetivo")
    print("4. Deletar Objetivo")
    print("5. Voltar ao menu principal")

    try:
        selecao = int(input())

        if selecao == 1:
            printObjetivos()
        elif selecao == 2:
            addObjetivo()
        elif selecao == 3:
            atualizarObjetivo()
        elif selecao == 4:
            deletaObjetivo()
    except TypeError:
        print("Erro de tipagem")

def addObjetivo():
    arquivo = arquivoHandler("5-6.txt","a")

    try:
        objetivo = input("Qual o objetivo do treino?: ")
        valor = float(input("Qual o valor que irá atingir?"))
        medida = input("Qual medida usou para o valor(m, s, min, km, ...)")

        arquivo.write(f"{objetivo}/{valor}/{medida}\n")

        print("Objetivo adicionado")

    except ValueError:
        print("Erro de tipagem")
        addObjetivo()

    arquivo.close();

def atualizarObjetivo():
    printObjetivos()

    arquivo = arquivoHandler("5-6.txt", "r")

    objetivoLista = arquivo.readlines()

    try:
        objetivo = input("Qual o objetivo que irá modificar?: ")
        valorModificado = float(input("Qual o valor a ser retirado?: "))

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
                    print("Objetivo atualizado")
                else:
                    print("Objetivo concluído!")
        arquivo.close()
        
        arquivo = arquivoHandler("5-6.txt", "w")   
        
        for i in newObjetivoList:
            arquivo.write(f"{i}")
    except TypeError:
        print("Erro de tipagem")
    
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

def sugereTreino():
    arquivo = arquivoHandler("treinos.txt", "r")

    arquivoList = arquivo.readlines()
    lengArquivo = len(arquivoList)

    if lengArquivo > 0:
        treinoEx = arquivoList[int(lengArquivo / 2)].split(";")

        #Sugere um treino com o objetivo 10% maior e tempo 10% menor
        
        print(f"Seu treino será: {float(treinoEx[2]) * 1.1} m em {int(treinoEx[3]) * 0.9} segundos")
        

    else:
        print("Nenhum treino para basear a sugestão")

## 7 ------------------------------
def funct_extra():

    file = open('7.txt', 'a')

    t = tempo.asctime(tempo.localtime())
    t = t.split(" ")

    decorrido = t[3].split(":")

    input('digite qualquer coisa e finalize a contagem:\n')

    x = tempo.asctime(tempo.localtime())
    x = x.split(" ")

    decorrido2 = x[3].split(":")

    print(f"Tempo de treino {int(decorrido2[2]) - int(decorrido[2])} foi de segundos\n")
    file.write(f"tempo de treino: {int(decorrido2[2]) - int(decorrido[2])} segundos\n")
    file.close()

main()
    
