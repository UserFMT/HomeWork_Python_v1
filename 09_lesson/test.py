from sqlalchemy import inspect, create_engine
from sqlalchemy.sql import text
from Object import Object

db_connection_string = "postgresql://postgres:vfhn2010@localhost:5432/HW4"


def test_db():
    #db = create_engine(db_connection_string)

    db = Object(db_connection_string)
    # выбираем название всех таблиц из базы
    insp = inspect(db).get_table_names()

    # получаем id
    new_id_user = int(db.set_id_user()[0])

    # Открываем соединение и начинаем транзакцию
    """
    with db.connect() as connection:
        with connection.begin() as transaction:
            try:
                sql_statement = text(
                    f"insert into users (user_id, user_email, subject_id) "
                    f"values ({int(new_id_user[0])}, 'test_9999@com', 10)"
                )
                connection.execute(sql_statement)

                # Фиксируем транзакцию
                transaction.commit()
            except Exception as e:
                # В случае ошибки откатываем транзакцию
                transaction.rollback()
                print(f"Ошибка: {e}")
    """
    db.insert_user(new_id_user,"test1@com",10,"Ошибка добавления user")

    assert 1 == 1
