import sqlite3
from src.camino.logger import log
from src.camino.config.setting import Settings
from src.camino.logger.api import Level
from src.camino.model.entities import Route

db_file = Settings.database_file()


class Database(object):

    connection = None
    cursor = None

    def __init__(self) -> None:
        log.message(Level.INFO, 'Building the DB Object')
        if Database.connection is None:
            try:
                Database.connection = sqlite3.connect(db_file)
                Database.cursor = Database.connection.cursor()
            except sqlite3.Error as oops:
                log.message(Level.ERROR, 'Error connecting to DB:' + str(oops))
            else:
                log.message(Level.INFO, 'Connection established')

        self.connection = Database.connection
        self.cursor = Database.cursor

    @staticmethod
    def load_routes():
        log.message(Level.INFO, 'Starting the load_routes')

        routes = []
        try:
            Database.cursor.execute("SELECT name, code FROM routes")

            rows = Database.cursor.fetchall()

            for row in rows:
                log.message("debug", 'loading:' + row[0])
                routes.append(row)
        except Exception as e:
            log.message(Level.ERROR, 'Error finding routes')
            raise e

        return routes

    @staticmethod
    def query_route(route_code):
        log.message(Level.INFO, 'Starting the query_route: ' + route_code)
        try:
            Database.cursor.execute("SELECT * FROM routes WHERE code = ?", [route_code])

            data = Database.cursor.fetchone()
            log.message(Level.DEBUG, 'loading:' + data[0])
            fields = [data[0], data[1], data[2], data[3], data[4], data[5]]
            route = Route(*fields)

        except Exception as e:
            log.message(Level.ERROR, 'Error finding routes')
            raise e

        return route

    @staticmethod
    def query_stages(route):
        log.message(Level.INFO, 'Starting the query_stages for route: ' + route[0])

        stages = []
        try:
            route_code = route[1]

            Database.cursor.execute("SELECT number, city, country, lat, lon FROM stages where code = ?", [route_code])
            rows = Database.cursor.fetchall()
            for row in rows:
                log.message("debug", 'loading:' + row[1])
                stages.append(row)
        except Exception as e:
            log.message(Level.ERROR, 'Error finding routes')
            raise e
        return stages

    @staticmethod
    def initialize_routes(data):
        log.message(Level.INFO, 'Starting the load_routes')
        sql1 = Settings.create_table_routes()

        sql2 = Settings.create_table_stages()

        sql3 = Settings.insert_into_routes()

        sql4 = Settings.insert_into_stages()

        log.message(Level.INFO, 'creating the routes/stages table')
        Database.cursor.execute(sql1)
        Database.cursor.execute(sql2)
        Database.connection.commit()

        for route in data['routes']:
            fields = (route['code'], route['name'], route['nickname'], route['count'],
                      route['length'], route['description'])

            log.message("debug", 'loading route->' + fields[1])
            Database.cursor.execute(sql3, fields)
            Database.connection.commit()

            stages = route['stages']
            for stage in stages:
                fields = (route['code'], stage['stage'], stage['city'], stage['country'],
                          stage['location'][0], stage['location'][1])

                log.message(Level.DEBUG, 'loading stages->' + str(fields[1]) + '/' + fields[2])
                Database.cursor.execute(sql4, fields)
                Database.connection.commit()
