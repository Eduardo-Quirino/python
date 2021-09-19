#Condicional If Elif Else
a = 10
b = 5
res =0
op = "$" #Mudar operador para obter resultados

if op == "+":
    res = a+b

elif op == "-":
    res = a-b

elif op == "*":
    res = a*b

elif op == "/":
    res = a/b
    
else:
    print("Operador invalido")

print(str(a)  + op + str(b) + " = " + str(res));  
