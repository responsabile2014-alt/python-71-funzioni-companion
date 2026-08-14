# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Scheda 54 - property
# Companion digitale - esempio principale

class Rettangolo:
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    @property
    def area(self):
        return self.base * self.altezza

r = Rettangolo(4, 3)
print(r.area)
