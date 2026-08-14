# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Laboratorio 10 - Creare il riepilogo di un ordine
# Companion digitale - soluzione del laboratorio

prodotti = ["Penna", "Quaderno", "Zaino"]
prezzi = [1.5, 3.2, 24.9]
quantita = [3, 2, 1]

righe = list()
subtotali = list()

for nome, prezzo, qta in zip(prodotti, prezzi, quantita):
    subtotale = prezzo * qta
    righe.append((nome, qta, subtotale))
    subtotali.append(subtotale)

for numero, (nome, qta, subtotale) in enumerate(righe, 1):
    print(numero, nome, qta, format(subtotale, ".2f"))

print("Totale ordine:", format(sum(subtotali), ".2f"))
