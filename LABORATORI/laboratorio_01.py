# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Laboratorio 1 - Un piccolo report delle vendite
# Companion digitale - soluzione del laboratorio

vendite = [1250.0, 980.5, 1430.25, 1100.0, 1675.75]

totale = sum(vendite)
media = totale / len(vendite)

print("Totale:", format(totale, ".2f"))
print("Media:", format(media, ".2f"))
print("Minimo:", format(min(vendite), ".2f"))
print("Massimo:", format(max(vendite), ".2f"))
