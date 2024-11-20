import os
os.system('cls')
import time as tempo

treinos = []
competicoes = []

def menu():
    print("\nMenu:")
    print("1. Adicionar Treino")
    print("2. Visualizar Treinos")
    print("3. Atualizar Treino")
    print("4. Excluir Treino")
    print("5. Adicionar Competição")
    print("6. Visualizar Competições")
    print("7. Atualizar Competição")
    print("8. Excluir Competição")
    print("9. Sair")

def adicionar_treino():
    treino = input("Digite os detalhes do treino: ")
    treinos.append(treino)
    print("Treino adicionado com sucesso!")

def visualizar_treinos():
    if not treinos:
        print("Nenhum treino cadastrado.")
    else:
        print("Treinos cadastrados:")
        for i, treino in enumerate(treinos, 1):
            print(f"{i}. {treino}")

def atualizar_treino():
    visualizar_treinos()
    index = int(input("Digite o número do treino que deseja atualizar: ")) - 1
    if 0 <= index < len(treinos):
        novo_treino = input("Digite os novos detalhes do treino: ")
        treinos[index] = novo_treino
        print("Treino atualizado com sucesso!")
    else:
        print("Índice inválido.")

def excluir_treino():
    visualizar_treinos()
    index = int(input("Digite o número do treino que deseja excluir: ")) - 1
    if 0 <= index < len(treinos):
        treinos.pop(index)
        print("Treino excluído com sucesso!")
    else:
        print("Índice inválido.")

def adicionar_competicao():
    competicao = input("Digite os detalhes da competição: ")
    competicoes.append(competicao)
    print("Competição adicionada com sucesso!")

def visualizar_competicoes():
    if not competicoes:
        print("Nenhuma competição cadastrada.")
    else:
        print("Competições cadastradas:")
        for i, competicao in enumerate(competicoes, 1):
            print(f"{i}. {competicao}")

def atualizar_competicao():
    visualizar_competicoes()
    index = int(input("Digite o número da competição que deseja atualizar: ")) - 1
    if 0 <= index < len(competicoes):
        nova_competicao = input("Digite os novos detalhes da competição: ")
        competicoes[index] = nova_competicao
        print("Competição atualizada com sucesso!")
    else:
        print("Índice inválido.")

def excluir_competicao():
    visualizar_competicoes()
    index = int(input("Digite o número da competição que deseja excluir: ")) - 1
    if 0 <= index < len(competicoes):
        competicoes.pop(index)
        print("Competição excluída com sucesso!")
    else:
        print("Índice inválido.")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            adicionar_treino()
        elif opcao == '2':
            visualizar_treinos()
        elif opcao == '3':
            atualizar_treino()
        elif opcao == '4':
            excluir_treino()
        elif opcao == '5':
            adicionar_competicao()
        elif opcao == '6':
            visualizar_competicoes()
        elif opcao == '7':
            atualizar_competicao()
        elif opcao == '8':
            excluir_competicao()
        elif opcao == '9':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

##2 ---------------------------------------


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


##4 ---------------------------------------

def import_treinos(treino,tempo,competicao):
    Q = int(input('Quantos treinos: '))

    for i in range(Q):
        treino = input("Digite a data do treino: \n")
        tempo = input("Digite o seu tempo: \n")
        treinos.append(treino)
        tempos.append(tempo)


    file = open('treinos.txt', 'a')
    for i in range(Q):
        file.write(f'treino do dia: {treinos[i]}, tempo: {tempos[i]}\n')



    j = int(input('Quantas competições: '))
    competicoes = []
    tempos2 = []

    for i in range(j):
        competicao = input("Digite o nome da competição: \n")
        tempo = input("Digite o seu tempo: \n")
        competicoes.append(competicao)
        tempos2.append(tempo)

    file = open('competições.txt', 'a')
    for i in range(j):
        file.write(f'competicao: {competicoes[i]}, tempo: {tempos2[i]}\n')
            
    import_treinos(treino,tempo,competicao)

## 5 ---------------------------------------


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

    menu()