#alterando e adicionando matriz
carros = [["Modelo", "HRV"], ["Fabricante", "Honda"], ["Ano", "2021"]]

carros.append(["Cor", "Prata"])

for l,c in carros:
    print( l + " | " + str(c)+"\n")
input()#janela fica aberta
