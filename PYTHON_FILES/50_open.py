# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Scheda 50 - open
# Companion digitale - esempio principale
# Questo esempio crea un file di esempio locale nella cartella corrente.

with open("esempio.txt", "w", encoding="utf-8") as f:
    f.write("Ciao")

with open("esempio.txt", "r", encoding="utf-8") as f:
    testo = f.read()

print(testo)
