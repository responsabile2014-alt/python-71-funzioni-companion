# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Laboratorio 2 - Da testi numerici a valori utilizzabili
# Companion digitale - soluzione del laboratorio

def positivo(numero):
    return numero > 0

testi = ["10", "-3", "25", "0", "8"]

numeri = list(map(int, testi))
positivi = list(filter(positivo, numeri))

print("Numeri:", numeri)
print("Positivi:", positivi)
print("Totale positivi:", sum(positivi))
