# 🛰️ Orbital-Overview 
This application is a playground for exploring satellites' orbits and their **ground tracks** on Earth.

---
# 📖 Background
The aim of this application is to track the orbit of a satellite. In order to achieve this goal the application download data of the satellite. The data are in **Two-Line Element (TLE)** format from [CelesTrak](https://celestrak.org/). TLE data format contains orbital data of an object that orbits around the Earth. For more info about this data check [here](https://it.wikipedia.org/wiki/Two-line_element).

TLE data are use by **Semplified Perturbation Models**, a set of 5 mathematical models (SGP, SGP4, SDP4, SGP8 and SDP8) used to calculate orbital state vectors of satellites and space debris relative to the Earth-centered inertial coordinate system. For more info about these models check [here](https://en.wikipedia.org/wiki/Simplified_perturbations_models).
---

## ✨ Functions (MVP)

- Download satellites' orbital data (TLE)
- Compute the default (ISS) satellite position for a given period
- Visualize a satellite's ground track on a 2D Earth map

---

## 💻 Installation and usage

### 1. Clone repo
```bash
git clone https://github.com/Torna99/Orbital-Overview
cd Orbital-Overview
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the main script
```bash
python orbit-viewer.py
```

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.




