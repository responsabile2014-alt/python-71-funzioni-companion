# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Laboratorio 3 - Costruire una classifica
# Companion digitale - soluzione del laboratorio

nomi = ["Anna", "Luca", "Sara", "Marco"]
punti = [82, 95, 88, 91]

classifica = sorted(zip(punti, nomi), reverse=True)

for posizione, (punteggio, nome) in enumerate(classifica, 1):
    print(posizione, nome, punteggio)
