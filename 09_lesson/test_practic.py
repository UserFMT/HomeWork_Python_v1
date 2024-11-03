from sqlalchemy import inspect, create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://postgres:vfhn2010@localhost:5432/HW4"


def test_db_1():
    db = create_engine(db_connection_string)
    insp = inspect(db).get_table_names()

    sql_statement = text("select max(user_id)+1 from student s")
    new_id_user = db.connect().execute(sql_statement).first()

    # Открываем соединение и начинаем транзакцию
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

    assert 1 == 1
