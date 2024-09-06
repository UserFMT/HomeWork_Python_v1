def is_year_leap(year_n):
    return True if (year_n % 4 == 0) else False


year_n = int(input('Введите год : '))
result = is_year_leap(year_n)
print(f'год {year_n} : {result}')
