from sgp4.api import Satrec
from sgp4.api import jday
import datetime
import numpy as np

# calculate lan and lon of the orbital object passed in the next 'minutes' minutes (for 2D rappresentation)
def calculate_orbit(tle_lines, minutes):

    satellite = Satrec.twoline2rv(tle_lines[0], tle_lines[1])
    start_time = datetime.datetime.now()

    # calculate lats and lons for each nexts minutess
    lats, lons = [],[]
    for m in range(0,minutes,1):
        t = start_time + datetime.timedelta(minutes=int(m))

        # julian date parameters
        jd, fr = jday(t.year, t.month, t.day, t.hour, t.minute, t.second)

        # calulcate error (code), position in kilometers from the center of earth in TEME coordinate and velocity km/s
        e, r, v = satellite.sgp4(jd, fr)

        # if isn't possible to calcute the orbital parameter for given date
        if not e == 0:
            print("Error during orbital computing!")
            exit()
        
        # calculate lat and lon (? WiP)
        x, y, z = r
        r_norm = np.linalg.norm(r)
        lat = np.degrees(np.arcsin(z / r_norm))
        lon = np.degrees(np.arctan2(y, x))
        lats.append(lat)
        lons.append(lon)
    
    return lats, lons

# temp for testing
def main():
    # ISS for testing
    tle = [ 
        "1 25544U 98067A   25249.16482935  .00011253  00000+0  20385-3 0  9992",
        "2 25544  51.6328 265.7109 0004205 306.5919  53.4683 15.50137885527726"
    ]

    # print the lats and lons
    lats, lons = calculate_orbit(tle, 120)
    for lat, lon in zip(lats, lons):
        print(f"Lat: {lat}, Lon: {lon}")

    import visualizer as vs
    vs.plot_2D_orbit(lats, lons, "ISS (ZARYA)")

if __name__ == "__main__":
    main()

        




