
# 🌱 Kasvihuone Automaatio

Raspberry Pi 4 -pohjainen automaatio- ja seurantajärjestelmä kasvihuoneelle. Projektin tavoitteena on kerätä ympäristötietoa (esim. lämpötila) sensoreilta, tallentaa data tietokantaan ja esittää se visuaalisesti web-käyttöliittymässä. Tulevaisuudessa järjestelmä mahdollistaa myös releohjaukset, kuten tuuletus, kastelu tai lämmitys automaattisesti.

---

## 🔧 Käytetyt teknologiat

- 🐍 Python 3
- 🌐 Flask (web-käyttöliittymä)
- 📊 Chart.js (graafit selaimessa)
- 💾 SQLite (paikallinen tietokanta)
- 💻 Raspberry Pi 4
- 🌡️ DS18B20-lämpötila-anturi
- 🕒 Cron (ajastus datan keruulle)

---

## 🖼️ Dashboard-näkymä

- Reaaliaikainen graafi päivän tai viikon lämpötiloista
- Statistiikka: **Korkein**, **alin** ja **keskiarvo**
- Responsiivinen käyttöliittymä
- Tumma ja vaalea teema (Dark Mode toggle)

---

## 🚀 Asennus & Käynnistys

### 1. Varmista riippuvuudet
```bash
pip3 install flask
```

### 2. Käynnistä sovellus
```bash
python3 app.py
```

### 3. Avaa selaimessa
```url
http://[raspberry_ip]:5000
```

Esimerkiksi: http://192.168.1.238:5000

---

## 🧪 Sensoridata ja tietokanta

### Tietokanta: `data/kasvihuone.db`

Tallennus tapahtuu seuraavalla taulurakenteella:

| id | timestamp (DATETIME) | temperature (REAL) |
|----|-----------------------|---------------------|

### Tietojen keruu:
Python-skripti `sensors/ds18b20_reader.py` lukee lämpötilan ja tallentaa sen tietokantaan.

Ajastus cronilla (esimerkki joka minuutti):
```bash
* * * * * /usr/bin/python3 /home/Kasvihuone/kasvihuone-automaatio/sensors/ds18b20_reader.py
```

---

## 📁 Projektirakenne

```bash
kasvihuone-automaatio/
├── app.py                    # Flask-sovellus
├── sensors/                  # Sensorien lukulogikka (esim. DS18B20)
│   └── ds18b20_reader.py
├── utils/                    # Apuskriptit (esim. tietokannan alustus)
├── static/
│   ├── css/
│   │   └── style.css         # Ulkoasu ja dark mode -tyylit
│   └── js/
│       └── script.js         # Chart.js + frontend-logiikka
├── templates/
│   └── index.html            # HTML-näkymä
├── data/                     # SQLite-tietokanta (gitignore estää sen seuraamisen)
├── requirements.txt
└── .gitignore
```

---

## 🛠️ Suunnitellut jatkokehitykset

- [ ] 💧 Mullan kosteusanturi
- [ ] 💡 Valoisuuden mittaus
- [ ] 🔁 Relemoduulin ohjaus (tuulettimet, kastelu)
- [ ] 📆 Kuukausinäkymä graafissa
- [ ] 📲 Mobiiliresponsiivisuus
- [ ] 🔐 Käyttöoikeudet / salasanasuojaus dashboardiin
- [ ] ☁️ Etäkäyttö (VPN / pilvipalvelin)

---

## 💡 Yhteystiedot

Projektin tarkoitus on oppia ja kehittää Python- ja automaatiotaitoja.  
Jos haluat tehdä oman version tai laajentaa tätä, voit forkata tai osallistua mukaan!

---

© 2025 – Kasvihuone Automaatio by Shogunium
