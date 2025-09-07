# 🛰️ Orbital-Overview 
This application is a playground for exploring satellites' orbits and their **ground tracks** on Earth.

---

# 📖 Background
The aim of this application is to track the orbit of a satellite. To achieve this, the application downloads the satellite’s orbital data in the **Two-Line Element (TLE)** format from [CelesTrak](https://celestrak.org/). A TLE describes the orbital parameters of an object orbiting Earth. For more information about TLEs, see [this reference](https://it.wikipedia.org/wiki/Two-line_element).
<br><br>
TLE data are used by Simplified Perturbation Models—a family of five mathematical models (SGP, SGP4, SDP4, SGP8, and SDP8)—to compute the orbital state vectors of satellites and space debris in relation to the Earth-centered inertial (ECI) coordinate system. For more details on these models, check [this page](https://en.wikipedia.org/wiki/Simplified_perturbations_models).

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




