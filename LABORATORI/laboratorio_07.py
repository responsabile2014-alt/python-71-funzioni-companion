# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Laboratorio 7 - Leggere un file e creare un riepilogo
# Companion digitale - soluzione del laboratorio
# Questo laboratorio crea un file di esempio locale nella cartella corrente.

with open("incassi.txt", "w", encoding="utf-8") as file:
    file.write("120.50\n80.00\n99.50\n")

incassi = list()

with open("incassi.txt", "r", encoding="utf-8") as file:
    for riga in file:
        incassi.append(float(riga.strip()))

print("Incassi:", incassi)
print("Totale:", format(sum(incassi), ".2f"))
print("Minimo:", format(min(incassi), ".2f"))
print("Massimo:", format(max(incassi), ".2f"))
