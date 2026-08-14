# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Scheda 24 - filter
# Companion digitale - esempio principale

def positivo(n):
    return n > 0

numeri = [-2, 0, 3, 5]
risultato = list(filter(positivo, numeri))
print(risultato)
