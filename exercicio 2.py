numero = int(input("Digite um numero de 1 a 10:"))

if 1 <= numero <=11:
    for i in range(1,11):
        print(numero, "x", i, "=", numero * i)
    else:
        print("numero invalido. Por favor insira um numero entre 1 e 10.")
