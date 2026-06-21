products_list =[
    {"name": "Headphones", "price": 25, "rating": 3.5}, 
    {"name": "Mouse", "price": 60 ,"rating": 4.2},
    {"name": "Laptop", "price": 800, "rating": 4.8}, 
]
def check_product(item):
    tax = item["price"] * 0.10
    total_price = item["price"] + tax 
    if item["rating"] >= 4.0:
        print(f"🔥 {item['name']} (Rating: {item['rating']}) is Top Rated! Total: {total_price}$")  
    else:
        print(f" 📦 {item['name']} (Rating: {item['rating']})  Total: {total_price}$")
for product in products_list:
    check_product(product)