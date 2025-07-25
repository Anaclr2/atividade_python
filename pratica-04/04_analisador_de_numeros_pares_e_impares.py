"""4- Analisador de Números Pares e Ímpares
Desenvolva um programa que classifica números inteiros como pares ou ímpares. O programa deve:

* Solicitar números inteiros até que o usuário digite "fim".  
* Informar se o número digitado é par ou ímpar.  
* Ao final, exibir a quantidade total de números pares e ímpares informados.  
* Tratar entradas inválidas com mensagens de erro apropriadas.  """
numeros_pares = 0
numeros_impares = 0
while True:
    entrada = input("Digite um número inteiro (ou 'sair' para encerrar): ")
    
    if entrada.lower() == "fim":
        break
    
    try:
        numero = int(entrada)
        
        if numero % 2 == 0:
            numeros_pares += 1
            print(f"{numero} é par.")
        else:
            numeros_impares += 1
            print(f"{numero} é ímpar.")
    
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

print(f"Total de números pares: {numeros_pares}")
print(f"Total de números ímpares: {numeros_impares}")
