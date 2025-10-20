"""
This is the entry point for the Camino Project.
"""

from view.api import View
from model.api import Model
from logger import log
import sys

log.message("info", 'Starting the Camino Weather Application')

log.message("debug", 'Creating the Model')
model = Model()

log.message("debug", 'Creating the View')
view = View(model)

log.message("debug", 'Initializing the View')
view.initialize()

log.message("debug", 'Running the View')
view.run()

log.message("info", 'Ending the Camino Weather Application')
sys.exit("Camino Weather Application has ended")
