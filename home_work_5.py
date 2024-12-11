from prices import prices
from phrases import phrases

def greet_client():
    print("Добрый день! Добро пожаловать в наш ресторан.")
    name = input("Как к вам можно обращаться? ")
    print(f"Рады вас видеть, {name}!")
    return name

def offer_dishes():
    print("\nВот наши блюда на сегодня:")
    for dish, phrase in phrases.items():
        print(f"{phrase} ({prices[dish]} руб. за порцию)")

def take_order():
    print("\nЧто бы вы хотели заказать?")
    order = {}
    for dish in prices:
        try:
            quantity = int(input(f"Сколько порций {dish} вы хотите? (введите 0, если не хотите): "))
            if quantity > 0:
                order[dish] = quantity
        except ValueError:
            print("Пожалуйста, введите целое число.")
    return order

def calculate_total(order):
    total = sum(prices[dish] * quantity for dish, quantity in order.items())
    discount = total * 0.15
    final_total = total - discount
    return total, discount, final_total

def print_receipt(order, total, discount, final_total):
    print("\nВаш чек:")
    print("-" * 30)
    for dish, quantity in order.items():
        price_per_portion = prices[dish]
        total_price = price_per_portion * quantity
        print(f"{dish}: {quantity} пор. × {price_per_portion} грн. = {total_price} грн.")
    print("-" * 30)
    print(f"Сумма без скидки: {total} грн.")
    print(f"Скидка (15%): {discount:.2f} грн.")
    print(f"Итого к оплате: {final_total:.2f} грн.")
    print("-" * 30)

def main():
    name = greet_client()
    offer_dishes()
    order = take_order()
    if not order:
        print(f"{name}, вы ничего не заказали. Будем рады видеть вас снова!")
        return
    total, discount, final_total = calculate_total(order)
    print_receipt(order, total, discount, final_total)

if __name__ == "__main__":
    main()