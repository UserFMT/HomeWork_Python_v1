from address import Address
from mailing import Mailing

to_address = Address("999888", "Москва", "ул.Ленина", "14a", "123")
from_address = Address("777555", "Владивосток", "ул.Петрова", "45/2", "45")

mailing1 = Mailing(to_address, from_address, 1459.23, "78945а555")

# Отправление <track> из <индекс>, <город>, <улица>, <дом> - <квартира> в
# <индекс>, <город>, <улица>, <дом> -<квартира>. Стоимость <стоимость> рублей.

print(f'Отправление {mailing1.track} из {mailing1.to_address.index},'
      f'{mailing1.to_address.sity}, {mailing1.to_address.street},{mailing1.to_address.house_number} - '
      f'{mailing1.to_address.apartment_number} в {mailing1.from_address.index},'
      f'{mailing1.from_address.sity}, {mailing1.from_address.street},'
      f'{mailing1.from_address.house_number} -{mailing1.from_address.apartment_number}.'
      f'Стоимость {mailing1.cost} рублей')
