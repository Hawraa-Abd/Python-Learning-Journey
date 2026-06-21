# 1. قائمة المنتجات
products_list = [
    {"name": "Headphones", "price": 25, "rating": 3.5}, 
    {"name": "Mouse", "price": 60, "rating": 4.2},
    {"name": "Laptop", "price": 800, "rating": 4.8}, 
]

# 2. دالة فحص وتقييم المنتج
def check_product(item):
    tax = item["price"] * 0.10
    total_price = item["price"] + tax 
    if item["rating"] >= 4.0:
        print(f"🔥 {item['name']} (Rating: {item['rating']}) is Top Rated! Total: {total_price}$")  
    else:
        print(f" 📦 {item['name']} (Rating: {item['rating']})  Total: {total_price}$")

# 3. دالة تطبيق الخصم
def apply_discount(product_name, original_price):
    if original_price > 100:
        final_price = original_price - 5
        print(f" 🎉 {product_name} has a discount! New price: {final_price}$")
    else:
        print(f" 📦 {product_name} price remains: {original_price}$")

# 4. تشغيل حلقة التكرار (تبدأ من بداية السطر)
for product in products_list:
    check_product(product)

# 5. استدعاء دالة الخصم بشكل منفصل (تبدأ من بداية السطر)
apply_discount("Chair", 120)
apply_discount("Book", 15)


def check_weather(temp):
    if temp >=35:
        print(f" The weather is hot! It is {temp} degrees.")
    else:
        print(f" The weather is nice! It is {temp} degrees.")
check_weather(40)
check_weather(22)
