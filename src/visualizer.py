import matplotlib.pyplot as plt
import cartopy.crs as ccrs

def plot_2D_orbit(lats, lons, obj_name, title="2D Ground Track"):

    # create a new plot of 12x6 inches and add axes
    plt.figure(figsize=(12,6))
    ax = plt.axes(projection=ccrs.PlateCarree())

    # basic earth map 
    ax.stock_img()
    ax.coastlines()

    # plot the trajectory 
    ax.plot(lons, lats, 'r-', linewidth=2, label=f"{obj_name} Track", transform=ccrs.Geodetic())


    # Highlight starting and end point
    ax.plot(lons[0], lats[0], 'go', markersize=8, label="Start")
    ax.plot(lons[-1], lats[-1], 'bo', markersize=8, label="End")

    plt.title(title, fontsize=14)
    plt.legend()

    plt.show()

