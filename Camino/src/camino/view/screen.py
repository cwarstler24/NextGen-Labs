import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import timedelta, date, datetime
from src.camino.view import plotter
from src.camino.config.setting import Settings


class Screen(tk.Tk):
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.protocol("WM_DELETE_WINDOW", quit)

        self.model = model

        routes = model.get_routes()
        today = date.today()
        model.get_weather(routes[0], today, False)
        desc = model.get_description('C1').desc(True)

        self.title("Camino de Santiago - Weather")
        self.geometry("800x900")
        self.resizable(False, False)
        icon = tk.PhotoImage(file=Settings.get_icon_name())
        self.iconphoto(True, icon)

        container = ttk.Frame(self)
        container.grid()

        self.notebook = ttk.Notebook(container)
        self.notebook.grid(row=0, column=0, sticky=tk.NSEW)

        self.status = ttk.Frame(container)
        self.status.grid()

        self.first = ttk.Frame(self.notebook)
        self.second = ttk.Frame(self.notebook)
        self.second.pack(fill=tk.BOTH, expand=True)
        self.third = ttk.Frame(self.notebook)
        self.third.pack(fill=tk.BOTH, expand=True)
        self.forth = ttk.Frame(self.notebook)
        self.fifth = ttk.Frame(self.notebook)

        self.notebook.add(self.first, text="Settings")
        self.notebook.add(self.second, text="Temp")
        self.notebook.add(self.third, text="Wind")
        self.notebook.add(self.forth, text="Rain")
        self.notebook.add(self.fifth, text="Elevation")

        # selected in OptionMenu
        self.route_selection = tk.StringVar(self)
        self.metric_selection = tk.StringVar()

        names = [entry[0] + ' - ' + entry[1] for entry in routes]

        # Set the default value of the variable
        self.route_selection.set(names[0])
        self.option_menu = ttk.OptionMenu(self.first, self.route_selection, names[0], *names)
        self.option_menu.grid(row=1, column=0)

        self.date_selection = tk.StringVar(self)
        self.end_date = date.today() + timedelta(days=10)
        self.start_date = date.today() + timedelta(days=-365)
        self.cal = DateEntry(self.first, selectmode='day', textvariable=self.date_selection,
                             mindate=self.start_date, maxdate=self.end_date)
        self.cal.grid(row=2, column=0)

        self.metric = ttk.Radiobutton(self.first, text="Metric", variable=self.metric_selection, value="metric")
        self.metric.grid(row=3, column=0)
        self.metric.invoke()
        self.imperial = ttk.Radiobutton(self.first, text="Imperial", variable=self.metric_selection, value="imperial")
        self.imperial.grid(row=4, column=0)

        self.update_button = ttk.Button(self.first, text="Update Screen", command=self.update)
        self.update_button.grid(row=5, column=0)

        self.image_map = tk.PhotoImage(file=Settings.get_image_name())
        image_label = ttk.Label(self.first, image=self.image_map)
        image_label.grid(row=5, column=1)

        self.description = ttk.Label(self.first, text=desc, wraplength=450)
        self.description.grid(row=6, column=1, pady=10)

        button_quit = ttk.Button(self.status, text="Quit", command=container.quit)
        button_quit.grid(row=1, column=3, padx=10, pady=10)

        self.route_label = ttk.Label(self.status, text="Route: " + names[0])
        self.route_label.grid(row=1, column=1, padx=10, pady=10)

        self.date_label = ttk.Label(self.status, text="Date: " + date.today().strftime("%m/%d/%y"))
        self.date_label.grid(row=1, column=2, padx=10, pady=10)

        self.update()

    def update(self):
        metric = True if self.metric_selection.get() == 'metric' else False

        where = self.route_selection.get().split(" - ")
        code = where[1]
        when = datetime.strptime(self.date_selection.get(), '%m/%d/%y').date()

        self.route_label.configure(text="Route: " + self.route_selection.get())
        self.date_label.config(text="Date: " + self.date_selection.get())

        self.update_button.config(text="Working...")
        self.update_button.update()

        stages_weather = self.model.get_weather(where, when, metric)

        self.update_button.config(text="Update Screen")
        self.update_button.update()

        desc = self.model.get_description(code).desc(metric)
        self.description.config(text=desc)
        self.description.update()

        for widget in self.second.winfo_children():
            widget.destroy()
        plotter.create_temp_plot(self.second, stages_weather, metric)

        for widget in self.third.winfo_children():
            widget.destroy()
        plotter.create_wind_plot(self.third, stages_weather, metric)

        for widget in self.forth.winfo_children():
            widget.destroy()
        plotter.create_rain_plot(self.forth, stages_weather, metric)

        for widget in self.fifth.winfo_children():
            widget.destroy()
        plotter.create_elevation_plot(self.fifth, stages_weather, metric)
