nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
media = (nota1 + nota2 + nota3) / 3
if media == 10:
   print("Aprovado com Distinção")
elif media >= 7:
   print("aprovado")
else:
   print("reprovado")