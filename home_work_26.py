from pymongo import MongoClient

client = MongoClient("<your_connection_string>")
db = client["shop"]
laptops = db["laptops"]

laptop = {
    'brand': 'Apple',
    'model': 'MacBook Pro 16',
    'price': 2500,
    'year': 2023,
    'specs': {'cpu': 'M2 Max', 'ram': '32GB', 'storage': '1TB SSD'}
}
laptops.insert_one(laptop)

laptops.insert_many([
    {'brand': 'Dell', 'model': 'XPS 15', 'price': 2000, 'year': 2022, 'specs': {'cpu': 'Intel i7', 'ram': '16GB', 'storage': '512GB SSD'}},
    {'brand': 'HP', 'model': 'Spectre x360', 'price': 1500, 'year': 2021, 'specs': {'cpu': 'Intel i5', 'ram': '8GB', 'storage': '256GB SSD'}},
    {'brand': 'Lenovo', 'model': 'ThinkPad X1', 'price': 2200, 'year': 2023, 'specs': {'cpu': 'Intel i9', 'ram': '32GB', 'storage': '1TB SSD'}}
])

first_laptop = laptops.find_one()
print("Первый ноутбук:", first_laptop)

expensive_laptops = laptops.find({'price': {'$gte': 2000}})
print("Ноутбуки с ценой >= 2000:")
for laptop in expensive_laptops:
    print(laptop)

specific_laptop = laptops.find_one({'brand': 'Apple', 'model': 'MacBook Pro 16'})
print("Ноутбук по бренду и модели:", specific_laptop)
