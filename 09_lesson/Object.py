from sqlalchemy import inspect, create_engine
from sqlalchemy.sql import text

class Object:

    __script = {
        "set":""
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

