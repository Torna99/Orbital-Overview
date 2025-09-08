import src.tle_loader as tle_loader
import src.orbit_simulator as orbit_simulator
import src.visualizer as visualizer
import os.path


STATIONS_TLE_URL = "https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&amp;FORMAT=tle" 
STATION = "ISS (ZARYA)"
ORBIT_MINUTES = 90

def main():

    all_tles = tle_loader.get_all_tle_files()

    # Downloading the TLEs if not present in the directory data
    if not all_tles: 
        tle_loader.download_tle(STATIONS_TLE_URL)
        print(f"{STATION}'s TLE downloaded!")
    else: 
        print("data dir not empty!")

    # choose orbital object TODO

    tle = tle_loader.get_tle(STATION)

    # compute orbits  
    lats, lons = orbit_simulator.calculate_orbit(tle, ORBIT_MINUTES)

    # plotting orbit
    visualizer.plot_2D_orbit(lats, lons, STATION)

if __name__ == "__main__":
    main()
