products = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 2500
}

discount={}
discounts=0.10
orignal_desc=0
for product,price in products.items():
    price=price-(price*discounts)
    discount[product]= price

print(discount)