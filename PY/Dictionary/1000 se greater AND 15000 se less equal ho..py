products = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 2500
}

for product,price in products.items():
    if price>1000 and price<15000:
        print(f"Product:{product} Price:{price}")