import time as tempo

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