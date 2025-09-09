import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from matplotlib.animation import FuncAnimation

# setting 2D figure
# # create a new plot of 12x6 inches and add axes
# fig = plt.figure(figsize=(12,6))
# ax = plt.axes(projection=ccrs.PlateCarree())

# # basic earth map 
# ax.stock_img()
# ax.coastlines()

def create_2D_earth():
    # create a new plot of 12x6 inches and add axes
    fig = plt.figure(figsize=(12,6))
    ax = plt.axes(projection=ccrs.PlateCarree())

    # basic earth map 
    ax.stock_img()
    ax.coastlines()

    return fig, ax

def track_2D_orbit(fig, ax, lats, lons, obj_name, title="2D Ground Track"):

    # plot the trajectory 
    ax.plot(lons, lats, '-', linewidth=2, label=f"{obj_name} Track", transform=ccrs.Geodetic())

    # Highlight starting and end point
    ax.plot(lons[0], lats[0], 'o', markersize=8, label=f"{obj_name} Start")
    ax.plot(lons[-1], lats[-1], 'o', markersize=8, label=f"{obj_name} End")

    plt.title(title, fontsize=14)
    plt.legend()

    return fig, ax

# TODO: i don't like this way
def show_plot():
    plt.show()


