customer = {
    "name": "Turjo",
    "age": 25,
    "occupation": "Software Engineer",
    "verified": True,
    # each key should be unique, key:val
}

print(customer["name"])
print(customer.get("age"))
# print(customer["na"])
# print(customer.get("ag"))
print(customer.get("Birth Year", 1997))
customer["name"] = "Nasir Uddin Ahmed"
print(customer["name"])
customer["birthdate"]="1997, 15 September"
print(customer["birthdate"])

