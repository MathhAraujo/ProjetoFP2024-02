Q = int(input('Quantos treinos: '))
treinos = []
tempos = []

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


