# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Laboratorio 5 - Analizzare un piccolo elenco di parole
# Companion digitale - soluzione del laboratorio

parole = ["python", "colab", "python", "dati", "colab", "python"]

uniche = set(parole)

print("Parole:", len(parole))
print("Uniche:", len(uniche))
print("Ordinate:", sorted(uniche))
print("Più lunga:", max(uniche, key=len))
