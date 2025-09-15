class Carro:
    carros = []
 # Classe Carro que representa um carro e mantém uma lista de todos os carros criados.
    
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        Carro.carros.append(self)
 # Método construtor que inicializa os atributos do carro e adiciona o carro à lista de carros.

    def __str__(self):
        return f' marca:{self.marca} / modelo:{self.modelo} / ano:{self.ano}'
 # Método que retorna uma representação em string do carro.
    
    @classmethod
    def listar_carros(cls):
        for carro in cls.carros:
            print(carro)
 # Método de classe que lista todos os carros criados.

carro_1 = Carro('Fiat', 'Uno', 2020)
carro_2 = Carro('Ford', 'Fiesta', 2019)
 # Criação de instâncias da classe Carro.

Carro.listar_carros()
# Chamada do método de classe para listar todos os carros.

