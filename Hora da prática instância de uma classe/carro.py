from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def __str__(self):
        status = 'ligado' if self._ligado else 'desligado'
        return f'{self.marca} {self.modelo} | Nº de portas: {self.portas} | Ligado: {status}'

#veiculo_portas = Carro('GM', 'Onix', 4)

#print(veiculo_portas)