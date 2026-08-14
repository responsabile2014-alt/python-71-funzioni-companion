# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Laboratorio 6 - Controllare se un modulo è completo
# Companion digitale - soluzione del laboratorio

campi = ["Anna", "Rossi", "anna@email.it", ""]

compilati = []
vuoti = []

for valore in campi:
    compilato = bool(valore)
    compilati.append(compilato)
    vuoti.append(not compilato)

print("Tutti i campi compilati:", all(compilati))
print("C'è almeno un campo vuoto:", any(vuoti))
print("Campi totali:", len(campi))
