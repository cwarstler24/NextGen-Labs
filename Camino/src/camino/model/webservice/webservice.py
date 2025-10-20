from src.camino.logger import log
from src.camino.config.setting import Settings
from src.camino.model.entities import Weather
import requests
from datetime import datetime


class WebService(object):
    def __init__(self):
        log.message("info", 'Building the WebService Object')

#   the JSON results look like:

# {
# "latitude": 43.16,
# "longitude": -1.2399998,
# "generationtime_ms": 0.03802776336669922,
# "utc_offset_seconds": 3600,
# "timezone": "Europe/Berlin",
# "timezone_abbreviation": "CET",
# "elevation": 177,
# "daily_units": {
#   "time": "iso8601",
#   "temperature_2m_max": "°C",
#   "temperature_2m_min": "°C",
#   "precipitation_sum": "mm",
#   "wind_speed_10m_max": "km/h"-1.24
# },
# "daily": {
#   "time": [
#       "2023-11-25"
#   ],
#   "temperature_2m_max": [
#       12.5
#   ],
#   "temperature_2m_min": [
#       6.2
#   ],
#   "precipitation_sum": [
#       0.1
#   ],
#   "wind_speed_10m_max": [
#       8.6
#   ]
#  }
# }

# the stage records looks like:
# (0, 'St. Jean Pied de Port', 'France', 43.16, -1.24)

    def call_weather_api(self, stage, day, metric):
        lat = float(stage[3])
        lon = float(stage[4])

        present = datetime.today().date()
        if day < present:
            url = Settings.get_historical_weather_uri(metric).format(lat=lat, lon=lon, day=day)
        else:
            url = Settings.get_current_weather_uri(metric).format(lat=lat, lon=lon)

        response = requests.get(url, headers={'User-agent': 'your bot 0.1'})
        response.raise_for_status()
        results = response.json()
        (number, city, country, lat, lon) = stage
        temp_min = results['daily']['temperature_2m_min'][0]
        temp_max = results['daily']['temperature_2m_max'][0]
        wind = results['daily']['wind_speed_10m_max'][0]
        try:
            gust = results['daily']['wind_gusts_10m_max'][0]
        except KeyError:
            gust = -1
        rain = results['daily']['precipitation_sum'][0]
        elevation = results['elevation']
        fields = [number, city, country, lat, lon,
                  temp_min, temp_max, wind, gust, rain, elevation]
        weather = Weather(*fields)
        return weather
