from veiculos import Carro, Moto

modelo_moto = Moto("Yamaha", "MT-07", 689)
modelo_carro = Carro("Toyota", "Corolla", 4)
modelo_moto2 = Moto("Honda", "CB500F", 471)
modelo_carro2 = Carro("Ford", "Focus", 5)
modelo_moto3 = Moto("Kawasaki", "Ninja 650", 649)
modelo_carro3 = Carro("Volkswagen", "Golf", 5)

veiculos = [modelo_moto, modelo_carro, modelo_moto2, modelo_carro2, modelo_moto3, modelo_carro3]

print("Lista de Veículos:")
for veiculo in veiculos:
    print(veiculo)
