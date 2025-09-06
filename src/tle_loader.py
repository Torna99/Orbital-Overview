import requests


TLE_URL = "https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&amp;FORMAT=tle" #temp Wip: togliere appena si fa file main

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
            with open(f"../data/{orbital_obj}.tle", "w") as f:
                f.write(tle_line1 + "\n")
                f.write(tle_line2 + "\n")
        else:
            print(f"Attenzione: dati incompleti per {lines[i].strip()} (riga {i})")
    

# return the TLE lines (2 lines) of a specific orbital object 
# obtained by a specific .tle file
def get_tle(orbital_object):

    with open(f"../data/{orbital_object}.tle") as f:
        tle_line1 = f.readline()
        tle_line2 = f.readline()

    return tle_line1, tle_line2

# temp for testing
def main():
    #download_tle(TLE_URL)
    r1,r2 = get_tle("ISS (ZARYA)")
    print(r1+r2)

if __name__ == "__main__":
    main()


