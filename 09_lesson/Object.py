from sqlalchemy import inspect, create_engine
from sqlalchemy.sql import text

class Object:

    __script = {
        "get_id":"select max(user_id)+1 from student s",
        "insert_user": "insert into users (user_id, user_email, subject_id) values ( :new_id, 'test_9999@com', 10)",
        "insert_student":"",
        "delete_student":"",
        "delete_user":""
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)


    def get_table_names(self):
        return self.__db.connect().dialect.get_table_names(self.__db.connect())


    def connect(self):
        self.__db.connect()
        pass


    def get_new_id(self):
        return self.__db.connect().execute(text(self.__script["get_id"])).first()


    def insert_user(self, new_id, error):
        self.__db.connect().begin()
        try:
            self.__db.connect().execute(text(self.__script["insert_user"], new_id = new_id))
            self.__db.connect().commit()
        except Exception as e:
            # случае ошибки откатываем транзакцию
             self.__db.connect().rollback()
             print(f"Ошибка: {error}")
