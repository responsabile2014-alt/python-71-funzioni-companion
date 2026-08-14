# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Scheda 38 - issubclass
# Companion digitale - esempio principale

class Animale:
    pass

class Cane(Animale):
    pass

print(issubclass(Cane, Animale))
print(issubclass(Animale, Cane))
