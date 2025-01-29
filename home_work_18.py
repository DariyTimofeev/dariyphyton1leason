import csv

# Читаємо файл і виводимо тільки аеропорти з України
with open('csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';');
    for row in reader:
        if row['iso_country'] == 'UA':
            print(row['name']);
