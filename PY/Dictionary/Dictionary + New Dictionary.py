products = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 2500
}

new_product={}

for productss ,price in products.items():
    if price>5000:
        new_product[productss]=price

print(new_product)