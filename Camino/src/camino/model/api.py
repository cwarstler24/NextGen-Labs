from src.camino.model.database.database import Database
from src.camino.logger import log
from src.camino.config.setting import Settings
from src.camino.config import reader
from threading import Thread, Lock
from src.camino.model.webservice.webservice import WebService


class Model(object):
    def __init__(self):
        self.db = Database()
        self.results = []
        self.results_lock = Lock()
        self.webservice = WebService()

    def get_routes(self):
        log.message("debug", "Loading routes from DB")
        while True:
            try:
                routes = self.db.load_routes()
                break
            except Exception:
                log.message("debug", 'DB not found')
                filename = Settings.route_config_file()
                log.message("debug", filename)
                data = reader.load_route_data(filename)
                self.db.initialize_routes(data)

        log.message("info", routes)
        return routes

    def get_weather(self, route, day, metric):
        stages = self.db.query_stages(route)
        self.results = []
        log.message("debug", "starting threads")
        threads = []
        for stage in stages:
            thread = Thread(target=self.talk_to_weather, args=[stage, day, metric])
            log.message("info", "starting for stage: " + str(stage[0]))
            thread.start()
            threads.append(thread)

        while threads:
            threads.pop().join()
            log.message("info", "thread ended ")

        return sorted(self.results, key=lambda x: x.number)

    def talk_to_weather(self, stage, day, metric):
        log.message("info", "calling the weather API")
        weather = self.webservice.call_weather_api(stage, day, metric)
        with self.results_lock:
            self.results.append(weather)

    def get_description(self, route_code):
        log.message("info", "calling  for code: " + route_code)
        route = self.db.query_route(route_code)
        return route
