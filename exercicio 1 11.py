# Função para encontrar o maior número entre três números
def encontrar_maior(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Função principal
def main():
    # Solicita que o usuário insira três números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))

    # Encontra o maior número usando a função encontrar_maior
    maior_numero = encontrar_maior(num1, num2, num3)

    # Mostra o maior número
    print("O maior número é:", maior_numero)

# Chama a função principal
if __name__ == "__main__":
    main()

