class Veiculo:
    def __int__(self,cor,placa,numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("ligando o motor")


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def estar_carregado(self):
        print("Não estou carregado")

moto = Motocicleta("preta", "abc-2145", 2)
moto.ligar_motor()

carro = Carro("branco","cva-0021",5)
carro.ligar_motor()

caminhao = Caminhao("roxo", "gfd-3123", 8)
caminhao.ligar_motor()
caminhao.estar_carregado()
