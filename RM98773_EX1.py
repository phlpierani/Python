faturamento_anual = float(input(" informe o valor do faturamento anual "))
assinatura = input(" escolha a sua assinatura:  BASIC / SILVER / GOLD / PLATINUM ")
valor_bonus = 0
if assinatura.upper() == "BASIC":
    valor_bonus = faturamento_anual *0.3
elif assinatura.upper() == "SILVER":
    valor_bonus = faturamento_anual *0.2
elif assinatura.upper() == "GOLD":
    valor_bonus = faturamento_anual *0.1
elif assinatura.upper() == "PLATINUM":
    valor_bonus = faturamento_anual *0.05

print(" o cliente deve pagar o bonus no valor de R${}".format(valor_bonus))
