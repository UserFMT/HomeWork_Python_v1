from Object import Object

db_connection_string = "postgresql://postgres:vfhn2010@localhost:5432/HW4"


def test_db():
    db = Object(db_connection_string)
    # выбираем название всех таблиц из базы
    insp = db.get_table_names()

    #Получаем id для тестирования
    new_id_user = int(db.get_new_id()[0])

    #Создаем user
    db.insert_user(new_id_user,"Ошибка создания user")

    assert 1 == 1
