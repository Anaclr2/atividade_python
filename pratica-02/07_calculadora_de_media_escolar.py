"""3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais."""

nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3
print("Nota 1: {:.2f}".format(nota1))
print("Nota 2: {:.2f}".format(nota2))           
print("Nota 3: {:.2f}".format(nota3))

print("Média: {:.2f}".format(media))