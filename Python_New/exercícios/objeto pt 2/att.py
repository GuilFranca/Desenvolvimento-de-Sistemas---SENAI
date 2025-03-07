# Crie um class motorista e um class carro, associe o carro ao motorista e possibilite que ele acelere o carro e também acrescente algo ao porta malas

# OBJ Humano
class Motorista:
    def __init__(self,nome):
        self.nome = nome
        self.carro = None
    
    def associarCarro(self,carro):
        self.carro = carro
        carro.motorista = self
        print(f"{self.nome} agora é o motorista do carro {carro.modelo}.")
    
    def acelerarCarro(self):
        if self.carro:
            self.acelerarCarro()
        else:
            print(f"{self.nome} não tem um carro associado para acelerar.")
    
    def adicionarPortaMalas(self,item):
        if self.carro:
            self.adicionarPortaMalas(item)
        else:
            print(f'{self.nome} não tem um carro associado para adicionar {item} ao porta-malas.')


# OBJ Carro
class Carro:
    def __init__(self,modelo):
        self.modelo = modelo
        self.motorista = None
        self.velocidade = 0
        self.portaMalas = []
    
    def acelerarCarro(self):
        self.velocidade += 10
        print(f'O {self.modelo} está à {self.velocidade}km por hora.')
    
    def adicionarPortaMalas(self,item):
        self.portaMalas.append(item)
        print(f'O {item} foi adicionado ao porta-malas do {self.modelo}')

motorista1 = Motorista('Guilherme')
carro1 = Carro('HB20')

motorista1.associarCarro(carro1)

motorista1.acelerarCarro()

motorista1.adicionarPortaMalas("Mala de viagem")

motorista1.acelerarCarro()

print("Porta-malas do carro:", carro1.portaMalas)
