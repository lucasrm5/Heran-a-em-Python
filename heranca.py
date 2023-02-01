class Veiculo:
    def __init__(self, rodas, marca):
        self.rodas = rodas
        self.marca = marca

    def ligar(self):
        print("Ligou o veículo!")

class Carro(Veiculo):
    def __init__(self, rodas, marca, teto_solar):
        super().__init__(rodas, marca)
        self.teto_solar = teto_solar

vehicle = Carro(4, "Ferrari", True)
print(vehicle.marca)
print(vehicle.teto_solar)
print(vehicle.rodas)
vehicle.ligar()

class Moto(Veiculo):
    def __init__(self, rodas, marca, carenagem):
        super().__init__(rodas, marca)
        self.carenagem = carenagem

    def empinar(self):
        print("Empinou a moto!")

moto = Moto(2, "Honda", False)
print(moto.carenagem)
moto.ligar()
moto.empinar()