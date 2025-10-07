# Lê o nome de usuário
nome = input ("Digite seu nome: ")
print(f"Olá, {nome}!")
# Cria uma lista para armazenar as notas 
notas = []

# lê 4 notas do usuário
for i in range(4):
    nota = float(input(f"Digite a {i + 1}a nota: "))
    notas.append(nota)
    
#Calcula a média das notas
media = sum(notas) / len(notas)

# Mostra as notas
print ("\n notss digitadas: ")
for i, nota in enumerate(notas, start=1 ):
    print(f"Nota {1}: {nota} ")
    
# Mostra a média
print(f"\n Média das notas: {media: .2f} ")