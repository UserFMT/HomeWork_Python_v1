from smartphone import Smartphone

catalog = [
    Smartphone("TTL", "12.0", "+7914 145 1456"),
    Smartphone("RRN", "01.2045V", "+7978 789 7896"),
    Smartphone("GMKH_RT", "0V_45", "+7912 123 1234")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
