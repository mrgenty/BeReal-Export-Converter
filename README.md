# **BeReal Export Converter 📸**
![Python](https://img.shields.io/badge/Python-3.7%2B-blue)  

**🔗 Questo progetto è indipendente e non affiliato a BeReal.**  
Uno script Python progettato per elaborare l'esportazione ai sensi del **GDPR** ricevuta da **BeReal**.  
Il tool converte le immagini **WebP** in **JPG**, aggiunge i metadati mancanti dai dati JSON forniti e organizza le foto in modo leggibile e utilizzabile.  

---

## 📜 **Licenza**
> 🔓 **Questo progetto è rilasciato sotto la [Licenza MIT](LICENSE).**  
Sentiti libero di usarlo e migliorarlo!  

![License: MIT](https://img.shields.io/badge/License-MIT-green)  

---

## 🌟 **Funzionalità**
✨ **Converte le immagini .webp esportate da BeReal in .jpg**  
🗺️ **Aggiunge metadati EXIF**:  
- 📍 **Posizione (GPS)**: Latitudine e Longitudine.  
- 🕒 **Data e ora di scatto**.  

📂 **Organizza le immagini convertite** in una directory `output`.  

---

## 🛡️ **Prima di iniziare**
### 🔍 **Richiedere una copia dei dati a BeReal**
Per utilizzare questo script, devi prima richiedere una copia dei tuoi dati personali a **BeReal**, come previsto dal **Regolamento Generale sulla Protezione dei Dati (GDPR)**.

### 📋 **Come fare:**
1. 📲 **Apri l'app BeReal**.  
2. ⚙️ Vai su **`Impostazioni`** > **`Assistenza`**.  
3. 📝 Contatta l'assistenza BeReal e **richiedi una copia dei dati**.  
4. 📩 Dopo qualche giorno, riceverai un'email con un link per scaricare un archivio ZIP contenente i tuoi dati.  

---

## 📂 **Preparazione dei file**
### 📦 **Cosa fare dopo aver scaricato il file ZIP**
1. 📂 **Estrai l'archivio ZIP ricevuto da BeReal**.  
2. 🔍 Individua i seguenti file/cartelle:  
   - 📁 **La cartella contenente le immagini**: `Photos/post`  
   - 📄 **Il file JSON**: `posts.json` (nella root dell'archivio ZIP)  
3. 🚚 **Sposta i file richiesti**:  
   - Sposta **tutti i file immagine** dalla cartella `Photos/post` e il file **`posts.json`** direttamente nella directory principale del progetto (accanto a `convert.py`).  
4. ⚙️ **Esegui lo script (convert.py)**.  

---

## 📋 **Requisiti**
💻 **Requisiti software:**  
- 🐍 **Python 3.7 o superiore**  
- 📚 **Librerie Python**:  
  - `opencv-python-headless`  
  - `piexif`  

📦 **Come installare le dipendenze:**  
```bash
pip install -r requirements.txt
```

---

## 🚀 **Come usare il progetto**
Ecco come eseguire lo script passo dopo passo:  

1️⃣ Assicurati di aver spostato tutti i file della cartella **Photos/post** e il file **posts.json** nella directory principale del progetto.  
2️⃣ Esegui lo script **convert.py** con Python:  
```bash
python convert.py
```
📂 Le immagini convertite appariranno nella directory **output**.  

---

## 📦 **Struttura del progetto**
```
📂 Bereal-Export-Converter
├── 📄 README.md
├── 📄 LICENSE
├── 📄 requirements.txt
├── 📄 convert.py
├── 📄 posts.json
├── 🖼️ 1-example-image.webp
├── 🖼️ 2-example-image.webp
└── 📂 output
    ├── 🖼️ 1-example-image.jpg
    └── 🖼️ 2-example-image.jpg
```

---

## 🙌 **Contributi**
💡 **Vuoi contribuire al progetto?**  
Fai una **fork** di questo repository, applica le tue modifiche e invia una **pull request**.  

Se hai bisogno di aiuto o hai domande, sentiti libero di aprire una **issue**.  
Contribuire ai progetti open-source è un ottimo modo per imparare e aiutare la community! 🚀  

---

## 📣 **Contattami**
📧 Se hai suggerimenti, domande o richieste di supporto, sentiti libero di contattarmi o aprire una **issue**.  
Contributi e feedback sono sempre benvenuti!  

---

## ⚠️ **Disclaimer**
> 🔒 **Questo progetto è indipendente e non affiliato a BeReal.**  

---

## 💖 **Supporta il progetto**
Se questo progetto ti è stato utile, **lascia una stella su GitHub!**  
[![Star on GitHub](https://img.shields.io/github/stars/mrgenty/BeReal-Export-Converter.svg?style=social)](https://github.com/mrgenty/BeReal-Export-Converter/stargazers)  
