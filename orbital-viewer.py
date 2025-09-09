
# TODO: questo codice richeide di passare come argomento del main le stazioni che si voglio visualizzare con 
# necessità di conoscerle a priori e "bruttezza" nel passare gli argomenti tramite doppie virgolette => sistemare 
# 

import src.tle_manager as tle_manager
import src.orbit_simulator as orbit_simulator
import src.visualizer as visualizer
import os.path
import sys
import math


STATIONS_TLE_URL = "https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&amp;FORMAT=tle" 
DEFAULT_STATION = "ISS (ZARYA)"
# ORBIT_MINUTES = 90
SIMULATION_SPEED = 100  # 1 = normal speed, 2 = double speed, etc

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
    all_tles = tle_manager.get_all_tle_files()
    if not all_tles: 
        tle_manager.download_tle(STATIONS_TLE_URL)
        print(f"{satellite}'s TLE downloaded!")
    else: 
        print("data dir not empty!")

    for satellite in satellites:

        tle = tle_manager.get_tle(satellite)
        print(f"\n{satellite}")
        print(*tle)

        orbit_duration = math.ceil(tle_manager.compute_orbit_duration(tle))
        print(f"Orbit duration: {orbit_duration}")

        # compute orbits  
        lats, lons = orbit_simulator.calculate_orbit(tle, orbit_duration)

        # plotting orbit
        visualizer.track_2D_orbit(fig, ax, lats, lons, satellite)

    sim_speed = (1000 * 60) / SIMULATION_SPEED
    visualizer.show_plot(orbit_duration, fig, sim_speed, f"2D Ground Track for {orbit_duration} min at {SIMULATION_SPEED}x speed")


if __name__ == "__main__":
    main()
