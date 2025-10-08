# Cria uma lista para armazenar os caracteres
caracteres = []

# Lisa de vogais
vogais = ['a', 'e', 'i', 'o', 'u']

# Lê 10 caracteres do usuário
for i in range(10):
    letra = input(f"Digite o {i + 1}o caractere: ").lower()
    
    caracteres.append(letra)
    
#Filtra as consoantes
consoantes = [c for c in caracteres if c not in vogais]

# Mostra as consoantes e a quantidade
print ("\n Consoantes digitadas: ")
for c in consoantes:
    print(c)
    
print(f"\n Total de consoantes: {len(consoantes)}")  