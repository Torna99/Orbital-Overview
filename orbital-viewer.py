
# WiP: questo codice richeide di passare come argomento del main le stazioni che si voglio visualizzare con 
# necessità di conoscerli a priori e "bruttezza" nel passare gli argomenti tramite doppie virgolette => sistemare 
# 

import src.tle_loader as tle_loader
import src.orbit_simulator as orbit_simulator
import src.visualizer as visualizer
import os.path
import sys


STATIONS_TLE_URL = "https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&amp;FORMAT=tle" 
DEFAULT_STATION = "ISS (ZARYA)"
ORBIT_MINUTES = 90

def main():

    # create Earth canvas
    fig, ax = visualizer.create_2D_earth()

    # Getting satellites to plot or the default
    satellites = []
    satellites = sys.argv[1:]
    if len(satellites) == 0: 
        print(f"No satellite selected: showing {DEFAULT_STATION}")
        satellites.append(DEFAULT_STATION)

    # Downloading the TLEs file if not present in the directory data
    all_tles = tle_loader.get_all_tle_files()
    if not all_tles: 
        tle_loader.download_tle(STATIONS_TLE_URL)
        print(f"{satellite}'s TLE downloaded!")
    else: 
        print("data dir not empty!")

    for satellite in satellites:

        tle = tle_loader.get_tle(satellite)
        
        # compute orbits  
        lats, lons = orbit_simulator.calculate_orbit(tle, ORBIT_MINUTES)

        # plotting orbit
        visualizer.track_2D_orbit(fig, ax, lats, lons, satellite)

    visualizer.show_plot()


if __name__ == "__main__":
    main()
