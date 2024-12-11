from pywebio.input import input,NUMBER
from pywebio.output import put_text


def calculate_ticket_price():
    while True:

        age = input("Введіть свій вік (або натисніть Enter для виходу):", type=NUMBER)

        if age is None:
            break

        if age < 6:
            price = "Безкоштовно"
        elif 6 <= age <= 12:
            price = "50 грн (знижка 50%)"
        elif 13 <= age <= 17:
            price = "75 грн (знижка 25%)"
        elif 18 <= age < 60:
            price = "100 грн (повна ціна)"
        else:  # age >= 60
            price = "70 грн (знижка 30%)"

        put_text(f"Вартість квитка: {price}")

calculate_ticket_price()