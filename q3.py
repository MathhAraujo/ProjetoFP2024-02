import os
os.system('cls')

treinos = [
   {"data": "15/01/2024", "distancia (km)": 5.0, "tempo (minutos)": 25.0, "localização": "Parque Da Tamarineira", "clima": "Ensolarado"},
    {"data": "28/02/2024", "distancia (km)": 10.0, "tempo (minutos)": 52.5, "localização": "Praia De Boa Viagem", "clima": "Nublado"},
    {"data": "05/03/2024", "distancia (km)": 5.0, "tempo (minutos)": 24.5, "localização": "Morro Da Conceição", "clima": "Chuvoso"},
]

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

filtrar_treinos()
