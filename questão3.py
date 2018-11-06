cont=0

pergunta1= input(" Telefonou para a vítima?")

if pergunta1 == 'sim':
  cont = cont + 1

pergunta2= input("Esteve no local do crime?")

if pergunta2 == 'sim':
  cont = cont + 1

pergunta3= input("Mora perto da vítima?")

if pergunta3 == 'sim':
  cont = cont + 1

pergunta4= input("Devia para a vítima?")

if pergunta4 == 'sim':
  cont = cont + 1

pergunta4= input("Já trabalhou com a vítima")

if pergunta4 == 'sim':
  cont = cont + 1


if cont == 2:
  print("Suspeita")

if cont == 3 or cont == 4:
  print ("Cúmplice")

if cont == 5:
  print ("Assassino")

if cont == 0:
  print( "Inocente")