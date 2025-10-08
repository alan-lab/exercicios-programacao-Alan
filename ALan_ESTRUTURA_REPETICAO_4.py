# Lista para armazenar os 20 números
numeros = []

# Lê 20 números inteiros do usuário
for i in range(20):
     num = int(input(f"Digite o {i + 1}o número inteiro: "))
     numeros.append(num)

# Separa os números pares e ímpares
pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 !=0]

# Imprime os três vetores
print("\n Vetor original: ")
print(numeros)

print("\n Vetor pares: ")
print(pares)

print("\n Vetor impares: ")
print(impares)