products = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 2500
}

cheap_product={}

for product,price in products.items():
    if price<=2500:
        cheap_product[product]=price


print(cheap_product)