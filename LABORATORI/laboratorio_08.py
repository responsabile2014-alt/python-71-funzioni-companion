# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Laboratorio 8 - Esplorare e modificare un oggetto
# Companion digitale - soluzione del laboratorio

class Prodotto:
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo

prodotto = Prodotto("Penna", 1.5)

print(type(prodotto) is Prodotto)
print(isinstance(prodotto, Prodotto))
print("Ha prezzo:", hasattr(prodotto, "prezzo"))
print("Prezzo:", getattr(prodotto, "prezzo"))

setattr(prodotto, "scorta", 100)
print("Attributi:", vars(prodotto))

delattr(prodotto, "scorta")
print("Ha scorta:", hasattr(prodotto, "scorta"))
