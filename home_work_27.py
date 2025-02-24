from pymongo import MongoClient

client = MongoClient("<your_connection_string>")
db = client["store"]
products = db["products"]

products.insert_many([
    {'name': 'Laptop', 'price': 1000, 'quantity': 10, 'category': 'electronics'},
    {'name': 'Phone', 'price': 500, 'quantity': 20, 'category': 'electronics'},
    {'name': 'Tablet', 'price': 300, 'quantity': 15, 'category': 'electronics'}
])

all_products = products.find()
for product in all_products:
    print(product)

product_by_name = products.find_one({'name': 'Laptop'})
print(product_by_name)

expensive_products = products.find({'price': {'$gt': 50}})
for product in expensive_products:
    print(product)

products_with_phone = products.find({'name': {'$regex': 'Phone', '$options': 'i'}})
for product in products_with_phone:
    print(product)

top_3_products = products.find().sort('quantity', -1).limit(3)
for product in top_3_products:
    print(product)

products.update_one({'name': 'Tablet'}, {'$set': {'category': 'electronics'}})

products.update_one({'name': 'Phone'}, {'$inc': {'quantity': 5}})

products.update_one({'name': 'Laptop'}, {'$mul': {'price': 0.5}})

product_to_delete = products.find_one({'name': 'Tablet'})
products.delete_one({'_id': product_to_delete['_id']})

products.delete_many({'quantity': 0})
