#Condicional If Elif Else
clima = "sol" #condição
dinheiro = 650 #condição
lugar = ""

if clima == "sol" and (dinheiro >= 300 and dinheiro <= 500):  # condição 1
    lugar = "clube"

else: #condição 2
    lugar = "cinema"

print("Vou ao " + lugar)

#AND
# V  V  = V
# V  F  = F
# F  V  = F
# F  F  = F

#OR
# V  V  = V
# V  F  = V
# F  V  = V
# F  F  = F