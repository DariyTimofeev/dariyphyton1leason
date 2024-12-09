# from practice import total
import PRAISES
import PRICE
# from practice import

restaurant_name = 'Пузата хата'
print()

total_cost = 0
discount = 15/100

borsh_quantity = input(PRAISES.MSG_FRAISES.format(rest=restaurant_name, dish='борщ', price=PRICE.borsh_price))
print(borsh_quantity)

syrniki_quantity = input(PRAISES.MSG_FRAISES.format(rest=restaurant_name, dish='сырники', price=PRICE.syrniki_price))
print(syrniki_quantity)

total_cost_borsh_discount = PRICE.borsh_price * discount
total_cost_borsh = PRICE.borsh_price - total_cost_borsh_discount
print('Общая сумма борща учитывая скидку:', total_cost_borsh)

total_cost_syrniki_discount = PRICE.syrniki_price * discount
total_cost_syrniki = PRICE.syrniki_price - total_cost_syrniki_discount
print('Общая сумма сырников учитывая скидку:', total_cost_syrniki)
total_cost_qqqqq = total_cost_syrniki + total_cost_borsh
print('Общая сума чека:', total_cost_qqqqq)


