from src.camino.view.screen import Screen


class View(object):
    def __init__(self, model):
        """
        This is the View class for the Camino Weather application.
        """
        self.model = model
        self.screen = None

    def initialize(self):
        self.screen = Screen(self.model)

    def run(self):
        self.screen.mainloop()
