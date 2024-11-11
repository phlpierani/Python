minutos = int(input("digite a minutagem da sua maquina: "))
fatorial = 1

for x in range (1, minutos + 1):
    fatorial *= x
print(f" a senha é LIBERDADE{fatorial}")

