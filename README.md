# BeReal Export Converter 📸
**Questo progetto è indipendente e non affiliato a BeReal.**
Uno script Python progettato per elaborare l'esportazione ai sensi del GDPR ricevuta da **BeReal**.
Il tool converte le immagini **WebP** in **JPG**, aggiunge i metadati mancanti dai dati JSON forniti e organizza le foto in modo leggibile e utilizzabile.

---

## 📜 Licenza
Questo progetto è rilasciato sotto la [Licenza MIT](LICENSE). Sentiti libero di usarlo e migliorarlo!
![License: MIT](https://img.shields.io/badge/License-MIT-green)

---

## 🌟 Funzionalità
- Converte le immagini `.webp` esportate da BeReal in `.jpg`.
- Aggiunge i seguenti metadati EXIF:
  - Posizione (latitudine e longitudine GPS).
  - Data e ora di scatto.
- Organizza le immagini convertite in una directory `output`.

---

## 🛡️ Prima di iniziare
### Richiedere una copia dei dati a BeReal
Per utilizzare questo script, devi prima richiedere una copia dei tuoi dati personali a **BeReal**, come previsto dal **Regolamento Generale sulla Protezione dei Dati (GDPR)**.

### Come fare:
1. **Apri l'app BeReal**.
2. Vai su `Impostazioni` > `Assistenza`.
3. Cerca l'opzione per contattare l'assistenza BeReal e richiedere una copia dei dati (non è presente un'opzione dedicata al momento)
4. Dopo qualche giorno, riceverai un'email con un link per scaricare un archivio ZIP contenente i tuoi dati.

---

## 📂 Preparazione dei file
1. Estrai l'archivio ZIP ricevuto da BeReal.
2. Individua i seguenti file/cartelle:
   - La cartella contenente le immagini: `Photos/post`
   - Il file JSON: `posts.json` (nella root dell'archivio ZIP)
3. Sposta questi elementi:
   - Sposta **tutti i file immagine presenti nella cartella `post`** e il file `posts.json` nella directory in cui si trova lo script.
4. Esegui lo script (convert.py).

---

## 📋 Requisiti
- Python 3.7 o superiore
- Librerie Python:
  - `opencv-python-headless`
  - `piexif`
---


🙌 Contributi

Contributi e suggerimenti sono benvenuti! Fai una fork di questo repository, applica le tue modifiche e invia una pull request.

