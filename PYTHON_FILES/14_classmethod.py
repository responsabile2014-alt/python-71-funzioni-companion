# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Scheda 14 - classmethod
# Companion digitale - esempio principale

class Persona:
    def __init__(self, nome):
        self.nome = nome

    @classmethod
    def anonima(cls):
        return cls("Sconosciuto")

p = Persona.anonima()
print(p.nome)
