print("Добрый день")
print("Как к вам можно обращаться ")

client_name = input()
print('Добрый день', client_name)
print('Хорошо')
print('У нас есть такое меню: ')
import price
print('Рекомендую вам взять место основного блюда борщ а на десерт сырники с изюмом и мёдом')
input('Вам подходит? ')
input('Сколько порций вы хотите заказать? ')
print('Хорошо')
print('Вам повезло так как у нас сегодня 15% скидка всем посетителям')
print('Приятного аппетита')
print('Вот ваш счёт')

syrniki = print('Сырники с изюмом и мёдом | ₴ 118,00 |')
borsch = print('Красный борщ | ₴ 182,00 |')

syrniki_price = 118
borsch_price = 182

total_amout = syrniki_price + borsch_price

total_amout_2 = total_amout
procent = 15

total_amout_3 = total_amout_2 - (total_amout_2 * 15 / 100)
print(total_amout_3)

print('Общая сума счёта:', total_amout_3, 'гривен')



