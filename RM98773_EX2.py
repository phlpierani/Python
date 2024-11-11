segunda = int(input(" digite quantos votos segunda-feira teve "))
terca = int(input(" digite quantos votos terca-feira teve "))
quarta = int(input(" digite quantos votos quarta-feira teve "))
quinta = int(input(" digite quantos votos quinta-feira teve "))
sexta = int(input(" digite quantos votos sexta-feira teve "))
maior = max(segunda, terca, quarta, quinta, sexta)
lista = (segunda, terca, quarta, quinta, sexta)
empate = lista.count(maior)
if empate >1:
    print("houve um empate")
else:
    vencedor = ''
    if segunda == maior:
        vencedor = 'segunda feira'
    elif terca == maior:
        vencedor = 'terca feira'
    elif quarta == maior:
        vencedor = 'quarta feira'
    elif quinta == maior:
        vencedor = 'quinta feira'
    elif sexta == maior:
        vencedor = ' sexta feira'
    print(f" o dia com mais votos foi {vencedor} com {maior} votos ")








