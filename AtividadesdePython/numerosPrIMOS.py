#lucas mendonça doria
#Eike Santos da Sé

numero = int(input("Digite seu número e descubra os números primos até ele: "))

for i in range(2, numero + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
