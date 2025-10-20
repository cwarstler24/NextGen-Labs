from typing import Any

import yaml
from schema import Schema, SchemaError, And
from src.camino.logger import log
from src.camino.logger.api import Level

route_schema = Schema({
    "routes": [{
        "name": lambda n: n.startswith("Camino"),
        "code": lambda n: len(n) == 2,
        "nickname": str,
        "count": And(int, lambda n: 1 <= n <= 100),
        "length": And(int, lambda n: 1 <= n <= 1100),
        "description": str,
        "stages": [{
            "stage": And(int, lambda n: 0 <= n <= 100),
            "city": str,
            "country": str,
            "location": [
                float, float
            ]
        }]
    }]
})


def load_route_data(route_file) -> Any:
    log.message(Level.INFO, 'Reading Route Yaml file')
    with open(route_file, 'r') as file:
        data = yaml.safe_load(file)

    try:
        route_schema.validate(data)
        log.message(Level.INFO, 'Route Yaml is valid')
    except SchemaError as se:
        log.message(Level.ERROR, 'Route Yaml is invalid')
        raise se

    return data
