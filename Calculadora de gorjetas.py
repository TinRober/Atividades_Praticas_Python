# Calculadora de Gorjetas

def calculadora_gorjeta():
    # Entrada
    valor_conta = float(input("Qual foi o valor total da conta? R$ "))
    valor_gorjeta = int(input("Qual porcentagem de gorjeta você gostaria de dar? (10, 12 ou 15): "))
    num_pessoas = int(input("Quantas pessoas vão dividir a conta? "))

    if num_pessoas <= 0:
        print("O número de pessoas deve ser maior que zero.")
        return

    # Cálculo
    gorjeta = valor_conta * (valor_gorjeta / 100)
    total_conta = valor_conta + gorjeta
    valor_por_pessoa = total_conta / num_pessoas

    # Saída
    print("\n--- Resultado ---")
    print(f" Conta (sem gorjeta): R$ {valor_conta:.2f}")
    print(f" Gorjeta: R$ {gorjeta:.2f}")
    print(f" Total da conta: R$ {total_conta:.2f}")
    print(f" Cada pessoa deve pagar: R$ {valor_por_pessoa:.2f}")
    print("------------------")

# Executa
calculadora_gorjeta()

 
