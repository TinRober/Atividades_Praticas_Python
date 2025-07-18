class ContaBancaria:
    contas = []
    """Classe para representar uma conta bancária."""
    
    # Método construtor que inicializa o titular, saldo e status da conta.
    def __init__(self, titular, saldo=0.0):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        ContaBancaria.contas.append(self)
    

    # Método para representar a conta como string, mostrando o titular e o saldo.
    def __str__(self):
        return f'Conta de {self._titular} com saldo de: R${self._saldo:.2f}'
   
    # Método de classe para ativar uma conta bancária pelo titular.
    @classmethod
    def ativar_conta(cls, titular):
        for conta in cls.contas:
            if conta._titular == titular:
                conta._ativo = True
                print(f'Conta de {titular} ativada.')
                return
        print(f'Conta de {titular} não encontrada.')
   
    # Método de classe para desativar uma conta bancária pelo titular.
    @classmethod
    def desativar_conta(cls, titular):
        for conta in cls.contas:
            if conta._titular == titular:
                conta._ativo = False
                print(f'Conta de {titular} desativada.')
                return
        print(f'Conta de {titular} não encontrada.')
    
    # Método de classe para listar todas as contas bancárias.
    @classmethod
    def listar_contas(cls):
        for conta in cls.contas:
            print(conta)
    
    # Propriedade para acessar o titular da conta.
    @property
    def titular(self):
        return self._titular
   


class ClienteBanco:
    clientes = []
    """Classe para representar um cliente bancário."""

    # Método construtor que inicializa os atributos do cliente e adiciona à lista de clientes.
    def __init__(self, nome, cpf, idade, email, telefone):
        self._nome = nome.title()
        self._cpf = cpf
        self._idade = idade
        self._email = email.lower()
        self._telefone = telefone
        ClienteBanco.clientes.append(self)

    # Método para representar o cliente como string, mostrando os detalhes do cliente.
    def __str__(self):
        return f'Cliente: {self._nome} / CPF: {self._cpf} / Idade: {self._idade} / Email: {self._email} / Telefone: {self._telefone}'
 
    # Método de classe para listar todos os clientes bancários.
    @classmethod
    def listar_clientes(cls):
        print("Lista de Clientes:")
        for cliente in cls.clientes:
            print(cliente)

    # Propriedades para acessar os atributos do cliente.
    @property
    def nome(self):
        return self._nome

    
    @property
    def cpf(self):
        return self._cpf

    @property
    def idade(self):
        return self._idade

    @property
    def email(self):
        return self._email

    @property
    def telefone(self):
        return self._telefone


# Exemplo de uso

cliente1 = ClienteBanco('ana silva', '123.456.789-00', 30, 'ana@gmail.com', '(11) 99999-0000')
cliente2 = ClienteBanco('joão souza', '987.654.321-00', 45, 'joao@hotmail.com', '(21) 98888-1111')
cliente3 = ClienteBanco('maria oliveira', '111.222.333-44', 28, 'maria@yahoo.com', '(31) 97777-2222')

conta_1 = ContaBancaria('ana silva', 1500.00)
conta_2 = ContaBancaria('joão souza', 2500.00)
conta_3 = ContaBancaria('maria oliveira', 3000.00)

# Impressão direta
print(conta_1)
print(conta_2)
print(conta_3)

# Ativar contas
ContaBancaria.ativar_conta('ana silva')
ContaBancaria.ativar_conta('joão souza')
ContaBancaria.ativar_conta('maria oliveira')

# Listar contas
ContaBancaria.listar_contas()

# Listar clientes
ClienteBanco.listar_clientes()
