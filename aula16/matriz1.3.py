#alterando matriz
carros = [["Modelo", "HRV"], ["Fabricante", "Honda"], ["Ano", "2021"]]

carros[2][1] = 2019
print(carros[1][1] + "\n")

for l,c in carros:
    print( l + " | " + str(c))
input()#janela fica aberta
