bread = input('Enter quantity of bread loafs >> ').strip()
bread_quantity = int(bread)
bread_price = 24.35
total_bread = bread_quantity * bread_price

butter = input('Enter quantity of butter, g >> ').strip()
butter_quantity = float(butter)
butter_price_kg = 320.16
butter_price_g = butter_price_kg / 1000
total_butter = butter_quantity * butter_price_g
total =  total_butter + total_bread
total = round(total, -1)
print('*' * 50)
print('RECEIPT')
print(f'Total amount of money for your purchase = {total}')
print('=' * 50)

