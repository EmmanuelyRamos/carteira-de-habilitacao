#carteira de habilitação
id = int(input("Digite a sua idade:"))
exame = input("Você passou no exame médico?: (s/n) ").lower() == "s"
violacoes = input("Você tem violações de trânsito?: (s/n) ").lower() == "s"
if (id >= 18 and exame and not violacoes):
  print ("Você pode dirigir")
else:
  print ("Você não pode dirigir")
