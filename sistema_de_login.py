print('digite o usuario: ')
usuario = input()
print('digite a senha: ')
senha = input()

def efetuar_login(usuario, senha):

    if usuario == "roberto" and senha == "32145":
        return True
    else:
        return False
# Chamada da função
if efetuar_login(usuario, senha):
    print("Login bem-sucedido!")
else:
    print("Usuário ou senha incorretos.")