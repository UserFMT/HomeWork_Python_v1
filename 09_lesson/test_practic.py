from sqlalchemy import inspect, create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://postgres:vfhn2010@localhost:5432/HW4"


def test_add_user():
    db = create_engine(db_connection_string)
    insp = inspect(db).get_table_names()
    sql_statement = text("select max(user_id)+1 from users s")
    new_id_user = db.connect().execute(sql_statement).first()
    new_email = 'TEST999@com'
    new_subject = 10
    # Открываем соединение и начинаем транзакцию
    with db.connect() as connection:
        with connection.begin() as transaction:
            try:
                sql_statement = text(
                    "insert into users (user_id, user_email, subject_id) "
                    "values (:new_id_user, :new_email , :new_subject)")
                """
                Можно оформить через params
                params = {
                    "new_id_user": int(new_id_user[0]),
                    "new_email": new_email,
                    "new_subject": new_subject
                }
                 и вызвать connection.execute(sql_statement,params)
                 или так как есть сейчас
                """
                connection.execute(sql_statement, {'new_email': new_email, 'new_id_user': int(new_id_user[0]), 'new_subject': new_subject})
                # Фиксируем транзакцию
                transaction.commit()
            except Exception as e:
                # В случае ошибки откатываем транзакцию
                transaction.rollback()
                print(f"Ошибка: {e}")

    sql_statement = text("select max(user_id) from users s")
    id_user = db.connect().execute(sql_statement).first()
    assert int(new_id_user[0]) == int(id_user[0])

    sql_statement = text("select count(1) from users s")
    count_after = db.connect().execute(sql_statement).first()

    # удаляем ранее созданный  элемент
    with db.connect() as connection:
        with connection.begin() as transaction:
            try:
                sql_statement = text(
                    f"delete from users where user_id={int(new_id_user[0])}"
                )
                connection.execute(sql_statement)
                # Фиксируем транзакцию
                transaction.commit()
            except Exception as e:
                # В случае ошибки откатываем транзакцию
                transaction.rollback()
                print(f"Ошибка: {e}")

    sql_statement = text("select count(1) from users s")
    count_before = db.connect().execute(sql_statement).first()

    assert int(count_after[0]) > int(count_before[0])


def test_edit_user():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from users s order by user_id desc")
    user_after = db.connect().execute(sql_statement).first()
    email_after = user_after.__getattribute__("user_email")
    id_user = user_after.__getattribute__("user_id")
    email_before  = 'TEST999@COM'

    #Фиксируем новое значение в email
    with db.connect() as connection:
        with connection.begin() as transaction:
            try:
                sql_statement = text(
                    f"update users set user_email = :email where user_id = :user_id"
                )
                connection.execute(sql_statement,{'email': email_before, 'user_id': id_user})
                # Фиксируем транзакцию
                transaction.commit()
            except Exception as e:
                # В случае ошибки откатываем транзакцию
                transaction.rollback()
                print(f"Ошибка: {e}")


    sql_statement = text("select * from users s where user_id = :user_id")
    user_before = db.connect().execute(sql_statement,{'user_id': id_user}).first()
    assert user_before.__getattribute__("user_email") != user_after.__getattribute__("user_email")
    assert user_before.__getattribute__("user_email") == email_before

    #Возвращаем первичное значение email
    with db.connect() as connection:
        with connection.begin() as transaction:
            try:
                sql_statement = text(
                    f"update users set user_email = :email where user_id = :user_id"
                )
                connection.execute(sql_statement, {'email': email_after, 'user_id': id_user})
                # Фиксируем транзакцию
                transaction.commit()
            except Exception as e:
                # В случае ошибки откатываем транзакцию
                transaction.rollback()
                print(f"Ошибка: {e}")
    sql_statement = text("select * from users s where user_id = :user_id")
    user_before = db.connect().execute(sql_statement, {'user_id': id_user}).first()
    assert user_before.__getattribute__("user_email") == user_after.__getattribute__("user_email")


def test_delete_user():
    db = create_engine(db_connection_string)
    #Создаем user для дальнейшего удаления
    with db.connect() as connection:
        with connection.begin() as transaction:
            try:
                sql_statement = text(
                    "insert into users (user_id, user_email, subject_id) "
                    "values (:new_id_user, :new_email , :new_subject)")
                connection.execute(sql_statement, {'new_email': 'TEST_NEW@COM', 'new_id_user': 999999,
                                                   'new_subject': 10})
                # Фиксируем транзакцию
                transaction.commit()
            except Exception as e:
                # В случае ошибки откатываем транзакцию
                transaction.rollback()
                print(f"Ошибка: {e}")

    # Проверяем что user  с user_id=99999 существует
    sql_statement = text("select * from users s where user_id = :user_id")
    user_before = db.connect().execute(sql_statement,{'user_id': 999999}).first()
    assert user_before is not None


    #Удаляем user
    with db.connect() as connection:
        with connection.begin() as transaction:
            try:
                sql_statement = text(
                    f"delete from users where user_id = :user_id"
                )
                connection.execute(sql_statement,{'user_id' : 999999})
                # Фиксируем транзакцию
                transaction.commit()
            except Exception as e:
                # В случае ошибки откатываем транзакцию
                transaction.rollback()
                print(f"Ошибка: {e}")

    sql_statement = text("select * from users s where user_id = :user_id")
    user_before = db.connect().execute(sql_statement,{'user_id': 999999}).first()
    assert user_before is None
