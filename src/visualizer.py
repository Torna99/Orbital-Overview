import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from matplotlib.animation import FuncAnimation

active_satellites = []

def create_2D_earth():
    # create a new plot of 12x6 inches and add axes
    fig = plt.figure(figsize=(12,6))
    ax = plt.axes(projection=ccrs.PlateCarree())

    # basic earth map 
    ax.stock_img()
    ax.coastlines()

    return fig, ax

def track_2D_orbit(fig, ax, lats, lons, obj_name):

    # plot the trajectory 
    ax.plot(lons, lats, '-', linewidth=2, label=f"{obj_name} Track", transform=ccrs.Geodetic())

    # Highlight starting and end point
    starting_position, = ax.plot(lons[0], lats[0], 'o', markersize=8, label=f"{obj_name} Start")
    active_satellites.append({"lats":lats, "lons":lons, "position point":starting_position})

    return fig, ax

# Used for animate the satellite
def update(frame):
    for satellite in active_satellites:
        satellite["position point"].set_data([satellite["lons"][frame]], [satellite["lats"][frame]])
    return [sat["position point"] for sat in active_satellites]

# Starts animation and plot the figure.
def show_plot(minutes, fig, velocity, title="2D Ground Track"):

    ani = FuncAnimation(fig, update, frames=minutes, interval=velocity, blit=True)

    plt.title(title, fontsize=14)
    plt.legend()
    plt.show()



