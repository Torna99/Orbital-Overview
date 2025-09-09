import requests
from pathlib import Path

DATA_PATH = (Path(__file__).resolve().parent).parent / "data"
TOT_MIN = 60 * 24

""" Download TLEs from URL and create for each orbital object """
def download_tle(TLEs_URL):

    # downloading TLEs
    response = requests.get(TLEs_URL)
    if response.ok:
        print("TLEs downloaded: ")
        tles = response.text
        print(tles)
    else:
        print("URL requests error: " + requests.status_codes + "!")
        exit()

    # creating files 
    lines = tles.splitlines()
    for i in range(0, len(lines), 3):
        if i + 2 < len(lines):
            orbital_obj = lines[i].strip()
            tle_line1 = lines[i+1].strip()
            tle_line2 = lines[i+2].strip()
            with open(f"{DATA_PATH}/{orbital_obj}.tle", "w") as f:
                f.write(tle_line1 + "\n")
                f.write(tle_line2 + "\n")
        else:
            print(f"Attenzione: dati incompleti per {lines[i].strip()} (riga {i})")
    
""" Return the TLE lines (2 lines) of a specific orbital object obtained by a specific .tle file """
def get_tle(orbital_obj):

    tle_path = DATA_PATH / f"{orbital_obj}.tle"
    tle_lines = []
    with open(tle_path) as f:
        tle_lines.append(f.readline())
        tle_lines.append(f.readline())

    return tle_lines

""" Return every TLE available in the data directory """
def get_all_tle_files():
    tle_files = []
    for file in DATA_PATH.glob("*.tle"):
        tle_files.append(file.stem)
    return tle_files

""" Calculate the orbit duration in minutes based on the mean motion (revolution per day) in the TLE """
def compute_orbit_duration(tle):

    # mean motion (revolution per day) is in column 53:63
    mean_motion = float(tle[1][52:63])
    minutes = TOT_MIN / mean_motion
    return minutes


