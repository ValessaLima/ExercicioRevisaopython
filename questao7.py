import random
lista1 = []
lista2 = []
lista3 = []

while len(lista1) < 10:
    numero = int(input())
    if numero not in lista1:
        lista1.append(numero)
        lista3.append(numero)


while len(lista2)  < 10:
    numero = int(input())
    if numero not in lista2:
        lista2.append(numero)
        lista3.append(numero)

lista1.sort()        
lista2.sort()
lista3.sort()

print(lista1)
print(lista2)
print(lista3)