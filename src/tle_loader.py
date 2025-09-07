import requests
from pathlib import Path

DATA_PATH = (Path(__file__).resolve().parent).parent / "data"

# download TLEs from URL and create for each orbital object
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
    

# return the TLE lines (2 lines) of a specific orbital object 
# obtained by a specific .tle file
def get_tle(orbital_obj):

    tle_path = DATA_PATH / f"{orbital_obj}.tle"
    tle_lines = []
    with open(tle_path) as f:
        tle_lines.append(f.readline())
        tle_lines.append(f.readline())

    return tle_lines



# temp for testing
# def main():
#     #download_tle(TLE_URL)
#     l = get_tle("ISS (ZARYA)")
#     print(l[0]+l[1])


# if __name__ == "__main__":
#     main()


