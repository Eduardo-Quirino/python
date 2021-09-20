#Loop While
#import os
carros = []
carro = input("Digite o nome do carro: ")

while carro != "0":
    carros.append(carro)
    carro = input("Digite outro carro: ")
    print("\n\nPARA SAIR DIGITE 0")
   
#os. system('cls')
for x in carros:
    print(x)

print("\n\nFim do programa!")
input()#janela fica aberta 