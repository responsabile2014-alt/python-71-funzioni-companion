# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Scheda 30 - hasattr
# Companion digitale - esempio principale

class Persona:
    def __init__(self):
        self.nome = "Anna"

p = Persona()
print(hasattr(p, "nome"))
print(hasattr(p, "eta"))
