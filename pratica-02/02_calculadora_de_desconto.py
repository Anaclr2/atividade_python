"""2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes."""

nome_do_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20
desconto = (preco_original * porcentagem_desconto) / 100
preco_final = preco_original - desconto

print("Produto: {}".format(nome_do_produto))
print("Preço original: R${:.2f}".format(preco_original))
print("Desconto: R${:.2f}".format(desconto))
print("Preço final: R${:.2f}".format(preco_final))