# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Scheda 60 - setattr
# Companion digitale - esempio principale

class Persona:
    pass

p = Persona()
setattr(p, "nome", "Anna")
print(p.nome)
setattr(p, "nome", "Luca")
print(p.nome)
