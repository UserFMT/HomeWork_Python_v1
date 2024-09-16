def month_to_season(num):
    if num in (12, 1, 2):
        print('Зима')
    elif num in (3, 4, 5):
        print('Весна')
    elif num in (6, 7, 8):
        print('Лето')
    elif num in (9, 10, 11):
        print('Осень')
    else:
        print('Введенное число не является номером месяца')


num = int(input('Введите номер месяца года : '))
month_to_season(num)
