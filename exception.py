
# exit code above 0 means crash

try:
    age = int(input("Enter Your Age"))
    print(age)

except ValueError:
    print("Invalid Error")