from abc import ABC, abstractmethod
from decimal import Decimal
class Veículo_pagamento(ABC):

    def __init__(self, valor_diaria=100):
        self.valor_diaria = valor_diaria



    @abstractmethod
    def calcular_valor_total(self, dias):
        pass


class Carro(Veículo_pagamento):

    def __init__(self, valor_diaria):
        super().__init__(valor_diaria)

    def calcular_valor_total(self, dias):
        total = self.valor_diaria * dias
        return total


class Moto(Veículo_pagamento):

    def __init__(self, valor_diaria):
        super().__init__(valor_diaria)

    def calcular_valor_total(self, dias):
       total = self.valor_diaria * dias
       if dias >= 7:
           total = total - total * Decimal("0.10")
       return total

class Caminhao(Veículo_pagamento):

    def __init__(self, valor_diaria):
        super().__init__(valor_diaria)

    def calcular_valor_total(self, dias):
        return (self.valor_diaria + 50) * dias