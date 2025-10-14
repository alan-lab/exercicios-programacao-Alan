# Criação de uma lista para armazenar os 5 números inteiros
numeros = []

# Leitura dos 5 números inteiros
for i in range(5):
    while True:
        try:
            num = int(input(f"Digite o {i+1}º número inteiro: "))
            numeros.append(num)
            break
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

# Calculando a soma e a multiplicação dos números
soma = sum(numeros)
multiplicacao = 1
for num in numeros:
    multiplicacao *= num

# Exibindo o resultado
print(f"\nNúmeros digitados: {numeros}")
print(f"Soma dos números: {soma}")
print(f"Multiplicação dos números: {multiplicacao}")

# Aqui está a linha em branco após o código
