class Motorista:
    def __init__(self, nome):
        self.nome = nome
        self.carro = None

    def associar_carro(self, carro):
        self.carro = carro
        carro.motorista = self
        print(f"{self.nome} agora é o motorista do carro {carro.modelo}.")

    def acelerar_carro(self):
        if self.carro:
            self.carro.acelerar()
        else:
            print(f"{self.nome} não tem um carro associado para acelerar.")

    def adicionar_ao_porta_malas(self, item):
        if self.carro:
            self.carro.adicionar_ao_porta_malas(item)
        else:
            print(f"{self.nome} não tem um carro associado para adicionar itens ao porta-malas.")

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.velocidade = 0
        self.porta_malas = []
        self.motorista = None

    def acelerar(self):
        self.velocidade += 10
        print(f"O carro {self.modelo} está agora a {self.velocidade} km/h.")

    def adicionar_ao_porta_malas(self, item):
        self.porta_malas.append(item)
        print(f"Item '{item}' adicionado ao porta-malas do carro {self.modelo}.")

# Exemplo de uso
motorista = Motorista("Guilherme")
carro = Carro("Fusca")

motorista.associar_carro(carro)
motorista.acelerar_carro()
motorista.adicionar_ao_porta_malas("Mala de viagem")
motorista.acelerar_carro()
print("Porta-malas do carro:", carro.porta_malas)
