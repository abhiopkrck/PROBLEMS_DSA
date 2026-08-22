products = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 2500
}

discount={}

discount_value=0.10
for product,price in products.items():
    if price>=2000:
        price=price-(price*discount_value)
        discount[product]=price
print(discount)