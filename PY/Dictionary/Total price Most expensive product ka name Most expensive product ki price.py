products = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 2500
}

total=0
higest=0
higest_product=None

for product,price in products.items():
    total=total+price
    if price>higest:
        higest=price
        higest_product=product
    
print("Total:",total)
print(f"Most_expensive_product:{higest_product}")
print(f"Most_expensive_product_price:{higest}")