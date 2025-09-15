# Contador de vogais e consoantes em uma frase

def contador_vogais_consoantes():
    # Entrada
    frase = input("Digite uma frase: ").lower()
    vogais = "aeiou"
    consoantes = "bcdfghjklmnpqrstvwxyz"
    
    contador_vogais = sum(1 for char in frase if char in vogais)
    contador_consoantes = sum(1 for char in frase if char in consoantes)
    
    # Saída
    print(f"Número de vogais: {contador_vogais}")
    print(f"Número de consoantes: {contador_consoantes}")

# Executa
contador_vogais_consoantes()

    