# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Scheda 28 - getattr
# Companion digitale - esempio principale

class Persona:
    def __init__(self):
        self.nome = "Anna"

p = Persona()
print(getattr(p, "nome"))
print(getattr(p, "eta", 0))
