# Pedra, Papel, Tesoura

import random

def pedra_papel_tesoura():
    options = ["pedra", "papel", "tesoura"]
    
    Pessoa = input("Escolha pedra, papel ou tesoura: ").lower()
    if Pessoa not in options:
        print("Escolha inválida! Tente novamente.")
        return
    else: print(f"Você escolheu: {Pessoa}")
    
    Computador = random.choice(options)
    print(f"Computador escolheu: {Computador}")


    if Pessoa == Computador:
        print("Empate!")
        return
    elif (Pessoa == "pedra" and Computador == "tesoura") or \
         (Pessoa == "papel" and Computador == "pedra") or \
         (Pessoa == "tesoura" and Computador == "papel"): 
        print("Você venceu o computador!")
    else:
        print("O computador venceu!")

# Executa
pedra_papel_tesoura()