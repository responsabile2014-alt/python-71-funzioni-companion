# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Scheda 45 - memoryview
# Companion digitale - esempio principale

dati = bytearray(b"ABC")
vista = memoryview(dati)
print(vista[0])
vista[0] = 90
print(dati)
