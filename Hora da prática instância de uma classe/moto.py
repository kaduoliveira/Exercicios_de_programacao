from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def __str__(self):
        status = 'ligado' if self._ligado else 'desligado'
        return f'{self.marca} {self.modelo} | Tipo:  {self.tipo} | Ligado: {status}'
    
#moto1 = Moto('Honda', 'CG125', 'urbana')

#print(moto1)