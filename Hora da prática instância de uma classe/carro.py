from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        #self.portas = portas
        self.cor = cor

    def __str__(self):
        status = 'ligado' if self._ligado else 'desligado'
        return f'{self.marca} {self.modelo} | Cor: {self.cor} | Ligado: {status}'

    def ligar(self):
        pass
    