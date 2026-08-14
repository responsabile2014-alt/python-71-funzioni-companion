# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Laboratorio 4 - Trovare i codici duplicati
# Companion digitale - soluzione del laboratorio

codici = ["A1", "B2", "A1", "C3", "B2", "D4"]

unici = set(codici)

print("Righe ricevute:", len(codici))
print("Codici distinti:", len(unici))
print("Elenco:", sorted(unici))
