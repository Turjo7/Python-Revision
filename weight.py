weight = input("Enter Weight: ")
new_weight = float(weight)
# print(type(new_weight))
select = input("Enter k for kg | p for pound: ")

if select == "k" or select == "K":
    print("Your weight in pound: ")
    print(2.20462262*new_weight)

elif select == "p" or select == "P":
    print("Your weight in Kg: ")
    print(0.45359237*new_weight)
