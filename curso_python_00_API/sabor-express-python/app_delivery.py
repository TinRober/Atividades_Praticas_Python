# app.py - API de pedidos de comida
import os

restaurantes = [{'nome':'Outback', 'categoria':'Australiana', 'ativo':False}, 
                {'nome':'Madero', 'categoria':'Brasileira', 'ativo':True},
                {'nome':'Pizza Hut', 'categoria':'Italiana', 'ativo':False},
                {'nome':'Paris 6', 'categoria':'Francesa', 'ativo':True}]  # Lista para armazenar os restaurantes cadastrados
                    
def exibir_nome_do_programa():
    ''' Função para exibir o nome do programa no terminal '''
    print('Sabor Expresso - API de pedidos de comida\n')

def exibir_opcoes():
    
    ''' 
    Função para exibir as opções disponíveis no terminal 
     inputs: nenhuma
     outputs: exibe as opções de cadastro, listagem, ativação, exclusão e saída
    '''

    print('Opções disponíveis:\n')
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Excluir restaurante')
    print('5. Sair\n')

def escolher_opcao():
    # opcao_escolhida = input('Escolha uma opção: ') nesse modelo os números devem ser tratados como strings,sem o uso de int() a função não funciona corretamente porque o input retorna uma string
    # Aqui, vamos tratar a entrada como inteiro para facilitar a lógica
    
    ''' 
    Função para escolher uma opção do menu
     inputs: nenhuma
     outputs: chama a função correspondente à opção escolhida
    '''

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_restaurante()
        elif opcao_escolhida == 4:
            excluir_restaurante()
        elif opcao_escolhida == 5:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        print('Entrada inválida. Por favor, insira um número válido.\n')
        main()

def opcao_invalida():
    
    ''' 
    Função para tratar opções inválidas 
     inputs: nenhuma
     outputs: exibe mensagem de opção inválida e retorna ao menu principal
    '''

    print('Opção inválida. Tente novamente.\n')
    
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    
    ''' 
    Função para voltar ao menu principal 
     inputs: espera o usuário digitar uma tecla
     outputs: retorna ao menu principal do programa
    '''

    input('\n Digite uma tecla para voltar ao menu ')
    main()

def main():
    
    ''' 
    Função principal que executa o programa 
     inputs: nenhuma
     outputs: exibe o nome do programa, opções e chama a função para escolher uma opção
    '''   

    os.system('cls')  # Limpa o terminal
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

def finalizar_app():
    
    ''' 
    Função para finalizar o aplicativo
     inputs: nenhuma
     outputs: exibe mensagem de finalização e limpa o terminal
    '''
    
    exibir_subtitulo('Finalizando o app')
    # Se você estiver no Linux ou Mac, use 'clear' em vez de 'cls'
    print('Finalizando o app\n')

def exibir_subtitulo(texto):
   
    ''' 
    Função para exibir subtítulos no terminal 
     inputs: texto (string)
     outputs: texto exibido no terminal
    '''

    os.system('cls')  # Limpa o terminal
    print (texto)
    print('\n')

def cadastrar_novo_restaurante():
    
    '''
    Função para cadastrar um novo restaurante
     inputs: nome_do_restaurante, categoria_do_restaurante
     outputs: dados_do_restaurante (dicionário com os dados do restaurante)
    '''

    exibir_subtitulo('Cadastrar novo restaurante')
    nome_do_restaurante = input(f'Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite o nome da categoria do restaurante do {nome_do_restaurante}: ')
    dados_do_restaurante = { 'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False }
    restaurantes.append(dados_do_restaurante)  # Adiciona o novo restaurante à lista
    print(f'O Restaurante "{nome_do_restaurante}" foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    
    ''' 
    Função para listar os restaurantes cadastrados 
     inputs: restaurantes (lista de dicionários com os dados dos restaurantes)
     outputs: exibe os dados dos restaurantes no terminal
    '''

    exibir_subtitulo('Listar restaurantes')
    
    print('Restaurantes cadastrados:\n')
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = restaurante['ativo']
        status = 'Ativado' if ativo else 'Desativado'
        print(f'- {nome_restaurante} | {categoria_restaurante} | {status}')
  
    voltar_ao_menu_principal()

def alterar_estado_restaurante(): 
    
    ''' 
    Função para ativar ou desativar o estado de um restaurante 
     inputs: nome_restaurante (string)
     outputs: altera o estado do restaurante na lista de restaurantes
    '''

    exibir_subtitulo('alterar estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
         restaurante_encontrado = True
         restaurante['ativo'] = not restaurante['ativo']
         mensagem = f'O estado do restaurante "{nome_restaurante}" foi ativado com sucesso!' if restaurante['ativo'] else f'O estado do restaurante "{nome_restaurante}" foi desativado com sucesso!'
         print(mensagem)
               
    if not restaurante_encontrado:
        print(f'O restaurante "{nome_restaurante}" não foi encontrado.\n')

    voltar_ao_menu_principal()

def excluir_restaurante():
    
    ''' 
    Função para excluir um restaurante da lista
     inputs: nome_restaurante (string)
     outputs: remove o restaurante da lista de restaurantes
    '''
   
    exibir_subtitulo('Excluir restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja excluir: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurantes.remove(restaurante)
            print(f'O restaurante "{nome_restaurante}" foi excluído com sucesso!\n')
            

    if not restaurante_encontrado:
        print(f'O restaurante "{nome_restaurante}" não foi encontrado.\n')

    voltar_ao_menu_principal()

if __name__ == '__main__':
    
    ''' Executa a função principal do programa '''
    
    main()