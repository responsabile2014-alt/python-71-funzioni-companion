# PYTHON: 71 FUNZIONI DA CAPIRE E USARE — Materiali digitali

Materiali digitali del libro **«PYTHON: 71 FUNZIONI DA CAPIRE E USARE»** di Tania Cilio
— Collana Python & Colab, Vol. 2.

Questa pagina è pubblica: per scaricare i materiali **non serve alcun account**.

---

## Scaricare tutto in una volta

Premi il pulsante **Code** in alto e scegli **Download ZIP**, oppure usa il link diretto:

[Scarica tutti i materiali (ZIP)](https://github.com/responsabile2014-alt/python-71-funzioni-companion/archive/refs/heads/main.zip)

---

## Aprire i notebook in Google Colab

Non serve scaricare niente: premi il pulsante e il notebook si apre direttamente in Colab.

**1. Le 71 funzioni, una per una**

[![Apri in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/responsabile2014-alt/python-71-funzioni-companion/blob/main/01_71_FUNZIONI_GOOGLE_COLAB.ipynb)

**2. Il Laboratorio finale (10 sfide)**

[![Apri in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/responsabile2014-alt/python-71-funzioni-companion/blob/main/02_LABORATORIO_FINALE.ipynb)

**3. Il Ripasso per famiglie (24 esercizi)**

[![Apri in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/responsabile2014-alt/python-71-funzioni-companion/blob/main/03_RIPASSO_PER_FAMIGLIE.ipynb)

> In Colab i file della sessione sono temporanei: se vuoi conservare le tue modifiche,
> usa **File → Salva una copia in Drive**.

---

## Che cosa contiene il pacchetto

### Notebook

| File | Contenuto |
|---|---|
| `01_71_FUNZIONI_GOOGLE_COLAB.ipynb` | Le 71 voci nello stesso ordine alfabetico del libro, da `abs()` a `__import__()`. Per ogni voce: il rimando alla scheda del libro, una domanda di previsione, l'esempio principale da eseguire, l'output atteso, una piccola modifica da provare e una cella libera per la tua prova. |
| `02_LABORATORIO_FINALE.ipynb` | Le 10 sfide del Laboratorio finale. Per ognuna: scenario, funzioni allenate, la sfida, una cella PROVA TU separata, l'output atteso, la soluzione e una variazione da provare. La soluzione non si trova mai nella stessa cella in cui provi l'esercizio. |
| `03_RIPASSO_PER_FAMIGLIE.ipynb` | Le stesse 71 voci raggruppate nelle otto famiglie della Mappa del libro, con 3 esercizi per famiglia (24 esercizi in totale). |

### Cartelle

| Cartella | Contenuto |
|---|---|
| `PYTHON_FILES/` | 71 file `.py`, uno per ogni voce del libro, numerati nello stesso ordine: da `01_abs.py` a `71___import__.py`. Contengono l'esempio principale della scheda, utili a chi preferisce eseguire Python sul proprio computer invece di usare un notebook. |
| `LABORATORI/` | 10 file `.py` con le soluzioni dei laboratori finali: da `laboratorio_01.py` a `laboratorio_10.py`. |

### File di testo

| File | Contenuto |
|---|---|
| `00_LEGGIMI.txt` | Le istruzioni complete del pacchetto. |
| `AGGIORNAMENTI.txt` | Gli eventuali aggiornamenti tecnici del volume. |

---

## Eseguire i file `.py` sul tuo computer

Dal terminale, spostati nella cartella e scrivi:

```
python nome_del_file.py
```

---

## Avvertenze

- `PYTHON_FILES/09_breakpoint.py` apre il debugger e ferma l'esecuzione: eseguilo soltanto se vuoi provarlo.
- `PYTHON_FILES/35_input.py` richiede un dato digitato da tastiera.
- Gli esempi che creano file lavorano soltanto su file di esempio creati dal programma stesso, nella cartella di lavoro corrente. In Google Colab i file della sessione sono temporanei.
- Negli esempi con `eval()`, `exec()`, `compile()` e `__import__()` usa esclusivamente valori scritti e controllati da te. Non eseguire mai testo proveniente dall'esterno.

---

## Versione di Python

Il libro e questi materiali sono stati verificati con riferimento a **Python 3.14.7**.
La versione realmente disponibile in Google Colab o in un altro ambiente può essere diversa
e può cambiare nel tempo. All'inizio di ogni notebook trovi una cella che mostra la versione
effettivamente in uso:

```python
import sys
print(sys.version)
```

---

## Gli altri volumi della collana

- **Vol. 1 — Python da Zero con Google Colab.** Guida pratica per principianti assoluti: le fondamenta di Python e l'esecuzione guidata del codice con Google Colab.
  Materiali: [python-da-zero-notebook](https://github.com/responsabile2014-alt/python-da-zero-notebook)
- **Vol. 2 — Python: 71 funzioni da capire e usare.** Questo volume.
- **Vol. 3 — Python in Pratica con Google Colab.** In preparazione.
- **Vol. 4 — Dati e Automazione con Python.** In preparazione.

---

© 2026 Tania Cilio. Tutti i diritti riservati.
Il libro contiene le spiegazioni complete; questi materiali servono per eseguire, modificare
e sperimentare il codice.
