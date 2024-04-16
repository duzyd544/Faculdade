nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))


if 0.0 <= nota1 <= 10.0 and 0.0 <= nota2 <= 10.0:
 media = (nota1 + nota2) / 2
print("A média das notas é:",media)


if media > 6:
    print("O aluno foi aprovado!")
    
elif media >= 4 and media < 6:
    print("Você está de recuperação.")
    
else:
    print("O aluno foi reprovado.")
