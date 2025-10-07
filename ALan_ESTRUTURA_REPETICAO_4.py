# Lê o nome de usuário
nome = input ("Digite seu nome: ")
print(f"Olá, {nome}!")
# Cria uma lista vaza para armazenar os números reais
numeros = []
# Lê 10 números reais do usuário
for i in range(10):
    num = float(input(f"Digite o número real {i + 1}: "))
    numeros.append(num)
# Mostra os números inteiros digitados
print("Os números digitados em ordem inversa são:")
for num in reversed(numeros):
    print(num)