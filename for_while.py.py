numero = 1
for _ in range(10):  # supondo um número de 0 a 9
    numero = int(input("Digite um número positivo: "))
    if numero < 0:
        print("Número negativo, tente novamente.")
    else:
        print(f"Número positivo: {numero}")
        break

while numero < 0:
    numero = int(input("Número negativo, tente novamente: "))
    if numero >= 0:
        print(f"Número positivo: {numero}")
        break