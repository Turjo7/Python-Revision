number = input("Enter Your Phone Number")
length = len(number)


number_dict = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

for i in number:
    print(f'''{number_dict.get(i)}''')
