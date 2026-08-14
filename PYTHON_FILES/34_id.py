# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Scheda 34 - id
# Companion digitale - esempio principale
# Nota: il numero restituito da id() cambia a ogni esecuzione.

a = [1, 2]
b = a
c = [1, 2]
print(id(a) == id(b))
print(id(a) == id(c))
