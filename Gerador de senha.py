#Gerador de senha

import random
import string

def gerador_senha(tamanho=12):
   # Conjuntos de caracteres
   letras_maiusculas = string.ascii_uppercase
   letras_minusculas = string.ascii_lowercase
   numeros = string.digits
   especiais = string.punctuation

   # Garantir que a senha tenha pelo menos um caractere de cada tipo
   senha = [
         random.choice(letras_maiusculas),
         random.choice(letras_minusculas),
         random.choice(numeros),
         random.choice(especiais)
    ]
   
    # Completar o resto da senha com caracteres aleatórios de cada tipo
   todos = letras_maiusculas + letras_minusculas + numeros + especiais
   senha += random.choices(todos, k=tamanho - 4)

    # Embaralhar a senha para garantir aleatoriedade
   random.shuffle(senha)
   
    # Juntar a lista em uma string
   return ''.join(senha)

# Gerar e exibir a senha
print("Senha gerada:", gerador_senha())