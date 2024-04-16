cardapio = {
   100: 1.20,
   101: 1.30,
   102: 1.50,
   103: 1.20,
   104: 1.70,
   105: 2.20,
   106: 1.10
}
codigo_produto = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade desejada: "))

if codigo_produto in cardapio:
    # Calculando o valor total do pedido
    preco_unitario = cardapio[codigo_produto]
    valor_total = preco_unitario * quantidade
    print("Valor a ser pago: R$", valor_total)
else:
    print("Produto não encontrado no cardápio.")


