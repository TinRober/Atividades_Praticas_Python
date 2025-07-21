class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    
    def __str__ (self):
        estado = "ligado" if self._ligado else "desligado"
        return f"{self.marca} {self.modelo} - Estado: ({estado})"
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def __str__ (self):
        estado = "ligado" if self._ligado else "desligado"
        return f"{self.marca} {self.modelo} ({estado}, {self.portas} portas)"

    
class Moto(Veiculo):    
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def __str__ (self):
        estado = "ligado" if self._ligado else "desligado"
        return f"{self.marca} {self.modelo} ({estado}, {self.cilindrada}cc)"

    
