from address import Address
from mailing import Mailing

To = Address("443004", "Самара", "Калининградская", "4", "23")
From = Address("665023", "Калининград", "Самарская", "23", "4")

mailing = Mailing(To, From, "850", "123456789")

print(f"Отправление {mailing.track} из {mailing.from_address.town}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.town}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
