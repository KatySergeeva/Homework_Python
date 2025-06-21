from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "15PRO", "+79270000000"),
    Smartphone("Samsung", "A50", "+79270000001"),
    Smartphone("Honor", "X5", "+79270000002"),
    Smartphone("Huawei", "Pura 70", "+79270000003"),
    Smartphone("Xiaomi", "Redmi 12C", "+79270000004")
]
for smartphone in catalog:
    print(f'{smartphone.brand} - {smartphone.model}. {smartphone.sub_number} .')
