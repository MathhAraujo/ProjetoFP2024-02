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
