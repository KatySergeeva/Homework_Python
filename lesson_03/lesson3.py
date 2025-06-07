from user import User
from card import Card

Alex = User("Alex")
""" Mark = User("Mark")
Marta = User("Marta") """

Alex.sayName()
Alex.setAge(33)
Alex.sayAge()
""" Mark.sayName()
Marta.sayName() """

card = Card("1234 5678 1234 5678", "11/28", "Alex F")
Alex.addCard(card)
Alex.getCard().pay(1000)
