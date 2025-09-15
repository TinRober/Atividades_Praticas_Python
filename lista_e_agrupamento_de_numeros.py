
numeros_de_1_a_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = [2, 4, 6, 8, 10]
numeros_impares = [1, 3, 5, 7, 9]
numeros_primos = [2, 3, 5, 7]



def escrever_numero():
    try:
        numero = int(input('Digite um numero: '))
        if numero in numeros_de_1_a_10:
            print(f'O numero {numero} está na lista de números de 1 a 10.')
        if numero in numeros_pares:
            print(f'O numero {numero} é par.')
        if numero in numeros_impares:
            print(f'O numero {numero} é ímpar.')
        if numero in numeros_primos:
            print(f'O numero {numero} é primo.')
        if numero not in numeros_de_1_a_10:
            print(f'O numero {numero} não está na lista de números de 1 a 10.')
    except ValueError:
        print('Por favor, digite um numero válido.')

escrever_numero()

repeat = input('Deseja repetir? (s/n): ')
while repeat.lower() == 's':
    escrever_numero()
    repeat = input('Deseja repetir? (s/n): ')
print('Programa encerrado.')
