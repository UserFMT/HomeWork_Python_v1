from sqlalchemy import inspect, create_engine
from sqlalchemy.sql import text

class Object:

    __script = {

        "new_id" : "select max(user_id)+1  from student s",
        "insert_user" : "insert into users (user_id, user_email, subject_id) "
                        "values ( :new_id, :new_email , :new_subject)",
        "insert_student" : "",
        "delete_student" : "",
        "delete-user" : "",
        "update_student" : ""
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)


    def set_id_user(self):
        tt = text(self.__script["new_id"])
        return (self.__db.connect().execute(text(self.__script["new_id"])).first())

    def connect(self):
        self.connect()
        pass

    def insert_user(self, id, email, subject,  error):
            self.__db.connect().begin()
            try:
                self.__db.connect().execute(text(self.__script["insert_user"]+
                                                 f", new_id = {id}, "
                                                 f"new_email = {email},"
                                                 f"new_subject = {subject}"))
                self.__db.connect()._transaction.commit()
            except Exception as e:
                # В случае ошибки откатываем транзакцию
                self.__db.connect()._transaction.rollback()
                print(f"Ошибка: {error}")



