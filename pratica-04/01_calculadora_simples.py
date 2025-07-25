"""1- Calculadora Simples
Crie um programa que simule uma calculadora básica com as seguintes funcionalidades:

* Solicite ao usuário dois números reais.  
* Peça a operação desejada (+, -, *, /).  
* Realize a operação escolhida e exiba o resultado.  
* Trate divisões por zero e operações inválidas com mensagens apropriadas.  

O programa deve continuar solicitando entradas até que uma operação válida seja realizada com sucesso."""

def calculadora():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Escolha a operação (+, -, *, /) ou 'sair' para encerrar: ").strip()

            if operacao == "sair":
                print("Programa encerrado.")
                break

            if operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            elif operacao == "/":
                if num2 == 0:
                    print("Erro: Divisão por zero não é permitida.")
                    continue
                resultado = num1 / num2
            else:
                print("Operação inválida. Tente novamente.")
                continue

            print(f"O resultado de {num1} {operacao} {num2} é: {resultado:.2f}")
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")   

if __name__ == "__main__":

    calculadora()
    