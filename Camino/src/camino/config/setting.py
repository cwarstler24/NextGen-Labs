"""
This is the single location to adjust the application configuration settings.
"""
import os


class Settings(object):
    dir_name = os.path.dirname(__file__)

    @staticmethod
    def logger_config_file() -> str:
        file_name = "logger.yaml"
        return os.path.join(Settings.dir_name, file_name)

    @staticmethod
    def database_file() -> str:
        file_name = "camino.db"
        return os.path.join(Settings.dir_name, "..", file_name)

    @staticmethod
    def route_config_file() -> str:
        file_name = "routes.yaml"
        return os.path.join(Settings.dir_name, file_name)

    @staticmethod
    def create_table_routes() -> str:
        return '''
            CREATE TABLE IF NOT EXISTS routes (
              code TEXT NOT NULL,
              name TEXT NOT NULL,
              nickname TEXT,
              count INTEGER,
              length INTEGER,
              description TEXT,
              PRIMARY KEY (code)
            ) WITHOUT ROWID;
        '''

    @staticmethod
    def create_table_stages() -> str:
        return '''
            CREATE TABLE IF NOT EXISTS stages (
              code TEXT NOT NULL,
              number INTEGER,
              city TEXT NOT NULL,
              country TEXT NOT NULL,
              lat REAL,
              lon REAL,
              PRIMARY KEY (code, number),
              FOREIGN KEY (code)
                   REFERENCES routes (code)
            ) WITHOUT ROWID;
        '''

    @staticmethod
    def insert_into_routes() -> str:
        return '''
            INSERT INTO routes(code, name, nickname, count, length, description)
              VALUES(?,?,?,?,?, ?) 
        '''

    @staticmethod
    def insert_into_stages() -> str:
        return '''
            INSERT INTO stages(code, number, city, country, lat, lon)
              VALUES(?,?,?,?,?,?) 
        '''

    @staticmethod
    def get_current_weather_uri(metric) -> str:
        if metric:
            return r'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&elevation=nan&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max&timezone=Europe%2FMadrid&forecast_days=1'
        else:
            return r'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&elevation=nan&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=Europe%2FMadrid&forecast_days=1'


    @staticmethod
    def get_historical_weather_uri(metric) -> str:
        if metric:
            return r'https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}&start_date={day}&end_date={day}&elevation=nan&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max&timezone=Europe%2FMadrid'
        else:
            return r'https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}&start_date={day}&end_date={day}&elevation=nan&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=Europe%2FMadrid'

    @staticmethod
    def get_image_name() -> str:
        file_name = "Mapa_Rutas.gif"
        image_dir = "images"
        return os.path.join(os.path.join(Settings.dir_name, image_dir), file_name)

    @staticmethod
    def get_icon_name() -> str:
        file_name = "camino.png"
        image_dir = "images"
        return os.path.join(os.path.join(Settings.dir_name, image_dir), file_name)