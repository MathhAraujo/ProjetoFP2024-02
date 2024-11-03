
registros = []

def registros_():
  
    nome = input("Me confirme seu nome: ")
    traquejo = input("Olá {}, me informe seu treino/competição: ")
    data = input("Me informe a data: ")
    distancia = float(input("Qual distância voçê percorreu: "))
    tempo = float(input("Quanto tempo durou: "))
    localiz = input("Onde ocorreu: ")
    condclimaticas = input("Como estava o tempo: ")

    newregister = registros(traquejo,data,nome,distancia,tempo,localiz,condclimaticas)
    registros.append(newregister)
    print("Registro adicionado, até a próxima!\n")
    



