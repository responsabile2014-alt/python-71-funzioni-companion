# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Scheda 15 - compile
# Companion digitale - esempio principale
# Usa esclusivamente valori controllati. Non usare input non affidabile.

codice = compile("2 + 3", "<string>", "eval")
risultato = eval(codice)
print(risultato)
