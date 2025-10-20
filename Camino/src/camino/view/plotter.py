from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from src.camino.logger import log
import matplotlib.pyplot as plt
import tkinter as tk

# turn off:  RuntimeWarning: More than 20 figures have been opened.
plt.rcParams.update({'figure.max_open_warning': 0})


def create_temp_plot(frame, stages_weather, metric):
    log.message("info", 'Building the temp plot')
    x_vals, y_vals = zip(*[(i.city, float(i.temp_max)) for i in stages_weather])
    x_vals2, y_vals2 = zip(*[(i.city, float(i.temp_min)) for i in stages_weather])

    fig, ax = plt.subplots(figsize=(8, 8))

    plt.plot(x_vals, y_vals, color='red', label="Max Temp")
    plt.plot(x_vals2, y_vals2, color='blue', label="Min Temp")

    plt.title("Temperature")
    if metric:
        plt.ylabel("Temperature (in Celsius)")
    else:
        plt.ylabel("Temperature (in Fahrenheit)")

    ax.legend(loc='best', frameon=False)

    plt.xticks(rotation=-90)
    plt.grid()
    plt.subplots_adjust(bottom=0.28)
    f0 = tk.Frame(frame)
    temp_canvas = FigureCanvasTkAgg(fig, f0)
    temp_canvas._tkcanvas.grid()
    f0.grid()


def create_rain_plot(frame, stages_weather, metric):
    log.message("info", 'Building the rain plot')
    x_vals, y_vals = zip(*[(i.city, float(i.rain)) for i in stages_weather])

    fig, ax = plt.subplots(figsize=(8, 8))

    plt.plot(x_vals, y_vals, color='green', label="Precipitation")

    plt.title("Precipitation")
    if metric:
        plt.ylabel("Precipitation (in Millimeters)")
    else:
        plt.ylabel("Precipitation (in Inches)")

    ax.legend(loc='best', frameon=False)

    plt.xticks(rotation=-90)
    plt.grid()
    plt.subplots_adjust(bottom=0.28)
    f0 = tk.Frame(frame)
    rain_canvas = FigureCanvasTkAgg(fig, f0)
    rain_canvas._tkcanvas.grid()
    f0.grid()


def create_wind_plot(frame, stages_weather, metric):
    log.message("info", 'Building the wind plot')
    x_vals, y_vals = zip(*[(i.city, float(i.wind)) for i in stages_weather])
    if stages_weather[0].gust != -1:
        log.message("warning", 'No Wind Gust data')
        x_vals2, y_vals2 = zip(*[(i.city, float(i.gust)) for i in stages_weather])

    fig, ax = plt.subplots(figsize=(8, 8))

    plt.plot(x_vals, y_vals, color='black', label="Wind Speed")
    if stages_weather[0].gust != -1:
        plt.plot(x_vals2, y_vals2, color='orange', label="Wind Gusts")

    plt.title("Wind")
    if metric:
        plt.ylabel("Wind Speed (in Kilometers/Hour)")
    else:
        plt.ylabel("Wind Speed (in Miles/Hour)")

    ax.legend(loc='best', frameon=False)

    plt.xticks(rotation=-90)
    plt.grid()
    plt.subplots_adjust(bottom=0.28)
    f0 = tk.Frame(frame)
    wind_canvas = FigureCanvasTkAgg(fig, f0)
    wind_canvas._tkcanvas.grid()
    f0.grid()


def create_elevation_plot(frame, stages_weather, metric):
    log.message("info", 'Building the elevation plot')

    if metric:
        x_vals, y_vals = zip(*[(i.city, float(i.elevation)) for i in stages_weather])
    else:
        x_vals, y_vals = zip(*[(i.city, (float(i.elevation) * 3.28084)) for i in stages_weather])

    fig, ax = plt.subplots(figsize=(8, 8))

    plt.plot(x_vals, y_vals, color='brown', label="Elevation")

    plt.title("Elevation")
    if metric:
        plt.ylabel("Elevation (in Meters)")
    else:
        plt.ylabel("Elevation (in Feet)")

    ax.legend(loc='best', frameon=False)

    plt.xticks(rotation=-90)
    plt.grid()
    plt.subplots_adjust(bottom=0.28)
    f0 = tk.Frame(frame)
    elevation_canvas = FigureCanvasTkAgg(fig, f0)
    elevation_canvas._tkcanvas.grid()
    f0.grid()