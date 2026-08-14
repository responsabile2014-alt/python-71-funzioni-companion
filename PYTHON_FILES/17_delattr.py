# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Scheda 17 - delattr
# Companion digitale - esempio principale

class Persona:
    pass

p = Persona()
p.nome = "Anna"
print(hasattr(p, "nome"))
delattr(p, "nome")
print(hasattr(p, "nome"))
