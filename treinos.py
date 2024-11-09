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




