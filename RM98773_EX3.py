impar, par = 0, 0
for x in range (1, 50, 2):
    print("VOCE ESTA DIGITANDO AS NOTAS DOS ALUNOS IMPARES")
    nota = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NUMERO {x}: "))
    impar += nota

for x in range (2, 51, 2):
    print("VOCE ESTA DIGITANDO AS NOTAS DOS ALUNOS PARES")
    nota = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NUMERO {x}: "))
    par += nota

media_impar = impar / 25
media_par = par / 25
print(" a media dos alunos impares foi {:.1f} e a media dos alunos pares foi {:.1f}".format(media_par, media_impar))

if impar > par:
    print("a maior media foi dos alunos impares")
elif par > impar:
    print("a maior media foi dos alunos pares")
else:
    print(" foi empate")



