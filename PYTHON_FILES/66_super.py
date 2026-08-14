# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Scheda 66 - super
# Companion digitale - esempio principale

class Persona:
    def __init__(self, nome):
        self.nome = nome

class Dipendente(Persona):
    def __init__(self, nome, ruolo):
        super().__init__(nome)
        self.ruolo = ruolo

d = Dipendente("Anna", "Controller")
print(d.nome)
print(d.ruolo)
