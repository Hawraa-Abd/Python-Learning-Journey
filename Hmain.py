user_profile = {
    "name": "Hawraa",
    "role": "programmer",
    "level": 3
}
print(user_profile)
print(user_profile["name"])
print(user_profile["role"])
user_profile["level"] = 4
user_profile["city"] = "Baghdad"
print("After update:")
print(user_profile)
del user_profile["city"]
print("After deleting city:")
print(user_profile)