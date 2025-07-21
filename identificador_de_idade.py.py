# Identificador_De_Idade.py
# Este programa verifica a idade do usuário e classifica como menor de idade, maior de idade
print('Bem-vindo ao programa de verificação de idade!')
print('Este programa irá verificar se você é menor de idade, maior de idade ou idoso.')

def definir_idade():
    idade = int(input('Digite sua idade: '))
    print(f'Sua idade é {idade}')

    if idade < 18:
        print('Você é menor de idade.')
    elif idade >= 18 and idade < 60:
        print('Você é maior de idade.')
    else:
        print('Você é idoso.')
    
    
definir_idade()