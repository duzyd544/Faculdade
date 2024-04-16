def converter_nota(nota):
    if nota >= 86:
        return 'A'
    elif nota >= 61:
        return 'B'
    elif nota >= 36:
        return 'C'
    elif nota >= 1:
        return 'D'
    else:
        return 'E'

# Receber a nota do usuário
nota = int(input("Digite a nota da prova: "))

# Converter e imprimir o conceito correspondente
conceito = converter_nota(nota)
print(conceito)

