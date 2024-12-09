import textwrap
from datetime import datetime
from decimal import Decimal, ROUND_DOWN

def validate_decimal_input(prompt, scale=4):
    """Запитує користувача та повертає коректний Decimal"""
    while True:
        try:
            value = Decimal(input(prompt)).quantize(Decimal(f'1.{"0" * scale}'), rounding=ROUND_DOWN)
            return value
        except Exception:
            print("Помилка вводу. Введіть число.")

def validate_integer_input(prompt):
    """Запитує користувача та повертає ціле число"""
    while True:
        try:
            value = int(float(input(prompt)))
            return value
        except Exception:
            print("Помилка вводу. Введіть ціле число.")

item_1_title = textwrap.shorten(input('Введіть назву першого товару: ').ljust(20, '.'), width=20, placeholder='...')
item_1_quantity = validate_integer_input('Введіть бажаєму кількість першого товару: ')
item_1_price = validate_decimal_input('Введіть ціну першого товару (до 4 знаків після коми): ')

item_2_title = textwrap.shorten(input('Введіть назву другого товару: ').ljust(20, '.'), width=20, placeholder='...')
item_2_quantity = validate_integer_input('Введіть бажаєму кількість другого товару: ')
item_2_price = validate_decimal_input('Введіть ціну другого товару (до 4 знаків після коми): ')

item_1_total_cost = (item_1_price * item_1_quantity).quantize(Decimal('1.0000'))
item_2_total_cost = (item_2_price * item_2_quantity).quantize(Decimal('1.0000'))

total_cost = (item_1_total_cost + item_2_total_cost).quantize(Decimal('1.0000'))

printing_template = '{}\t\t{:>5}\t\t{:>10}\t\t{:>10}'

print('\n\n')
print('фіскальний чек'.capitalize().center(80, ' '))
print('магазин "все для дому"'.upper().center(80))
print(f'\n{"Товар":<20}\t\t{"Кількість":>5}\t\t{"Ціна":>10}\t\t{"Вартість":>10}')
print(printing_template.format(item_1_title, item_1_quantity, f"{item_1_price:.4f}", f"{item_1_total_cost:.4f}"))
print(printing_template.format(item_2_title, item_2_quantity, f"{item_2_price:.4f}", f"{item_2_total_cost:.4f}"))
print('-' * 80)
print(printing_template.format(
    "ВСЬОГО".ljust(20),
    '',
    '',
    f"{total_cost:.4f}"
))
print(datetime.now().strftime('%d-%m-%Y %H:%M:%S').rjust(80))
print('\n\n')