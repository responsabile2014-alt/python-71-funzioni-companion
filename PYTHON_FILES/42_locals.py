# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Scheda 42 - locals
# Companion digitale - esempio principale
# Nota: il contenuto dipende dall'ambiente di esecuzione.

def calcola():
    prezzo = 100
    sconto = 20
    finale = prezzo - sconto
    print(locals()["finale"])

calcola()
