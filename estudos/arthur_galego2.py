# 2- Tuple VS List	

#LIST - mutavel(crescimento, edição de numeros, adição e subtração)

a = []
a.append(1)
print(a)

a.append(2)
print(a)
print(id(a))
a.append(3)
print(a)
print(id(a))

#TUPLE - imutavel(representar algo para coordenadas x e y e isso nunca mudará)

x = (1,2)
x.append(3) #ERROR
x[0] = 3 #ERROR

