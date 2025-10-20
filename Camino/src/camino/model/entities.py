
from dataclasses import dataclass


@dataclass(frozen=True)
class Weather(object):
    number: int
    city: str
    country: str
    lat: float
    lon: float
    temp_min: float
    temp_max: float
    wind: float
    gust: float
    rain: float
    elevation: int

    def __str__(self):
        return f"{self.number} {self.city} - {self.temp_max}"


@dataclass(frozen=True)
class Route(object):
    code: str
    name: str
    nickname: str
    count: int
    length: int
    description: str

    def desc(self, metric):
        if metric:
            units = "Km"
            length = self.length
        else:
            units = "Miles"
            length = int(self.length * 0.621)
        return f"The {self.nickname} is a {self.count} stage route of {length} {units}. {self.description}"
