from pywebio.input import input
from pywebio.output import put_text


def zoo_ticket_price():
    age = input("Введите ваш возраст:", type="number")

    if age < 6:
        price = 0
        message = "Дети до 6 лет посещают зоопарк бесплатно."
    elif 6 <= age <= 12:
        price = 50
        message = f"Дети от 6 до 12 лет получают скидку 50%. Стоимость билета: {price} грн."
    elif 13 <= age <= 17:
        price = 75
        message = f"Подростки от 13 до 17 лет получают скидку 25%. Стоимость билета: {price} грн."
    elif 18 <= age < 60:
        price = 100
        message = f"Взрослые от 18 до 60 лет платят полную стоимость. Стоимость билета: {price} грн."
    else:
        price = 70
        message = f"Пенсионеры от 60 лет получают скидку 30%. Стоимость билета: {price} грн."

    put_text(message)

    if __name__ == "__main__":
        zoo_ticket_price()