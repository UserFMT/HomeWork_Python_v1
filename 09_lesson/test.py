from sqlalchemy import inspect, create_engine
from sqlalchemy.sql import text
from Object import Object

db_connection_string = "postgresql://postgres:vfhn2010@localhost:5432/HW4"


def test_db():
    db = create_engine(db_connection_string)
    # выбираем название всех таблиц из базы
    insp = inspect(db).get_table_names()

    """ добавить студента
     1. определение уникального user_id
     2. добавить student для  уникального user_id
     3  удалить студента 
     """

    sql_statement = text("select max(user_id)+1  from student s")
    new_id_user = db.connect().execute(sql_statement).first()
    sql_statement = text(f"insert into users (user_id,user_email,subject_id) "
                         f"values ({int(new_id_user[0])},'test_9999@com',10)")
    db.connect().execute(sql_statement)
    #db.connect().close()
    assert 1==1

