TipoDaCarne = str(input("Qual carne vai querer hoje? File duplo?, Alcatra? ou Picanha?"))

Quantidade = int(input("Digame quanto kilos vai querer? (Obs;s� vendemos por kilo e n�o kilo(s) e meio:("))

tipoPagamento = str(input("Como deseja pagar? Cart�o ou Dinheiro?"))

vFileAt5 = 4.90 
vAlcatraAt5 = 5.90
vPicanhaAt5 = 6.90

vFileAcim5 = 5.80 
vAlcatraAcim5 = 6.80
vPicanhaAcim5 = 7.80

Valor = 0

if (TipoDaCarne == "File duplo"):
  if (Quantidade <= 5):
    Valor = Quantidade*vFileAt5
  if (Quantidade >5):
    Valor = Quantidade*vFileAcim5


if (TipoDaCarne =="Alcatra"):
  if (Quantidade <= 5):
    Valor = Quantidade*vAlcatraAt5
  if (Quantidade >5):
    Valor = Quantidade*vAlcatraAcim5

if (TipoDaCarne =="Picanha"):
  if (Quantidade <= 5):
    Valor = Quantidade*vPicanhaAt5
  if (Quantidade >5):
    Valor = Quantidade*vPicanhaAcim5

print ("Aqui est� o sua nota fiscal:")
print ("tipo da carne:%s"%(TipoDaCarne))
print ("Quantidade:%d kilos"%(Quantidade))
print ("Pre�o total:%d  Reais"%(Valor))
print ("Pagamento:%s"%(tipoPagamento))

desconto = 0
if (tipoPagamento == "Cart�o"):
  desconto = (Valor*5)/10
  print ("Desconto :%d real(is)"%(desconto))
  
  x = Valor - desconto
  print ("valor a pagar:%d Reais"%(x))
else:
  print ("Sem Desconto:")
