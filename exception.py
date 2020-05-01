
# exit code above 0 means crash

try:
    age = int(input("Enter Your Age"))
    print(age)
    k=5/0
    print(k)

except ZeroDivisionError:
    print("Can Not Divide by Zero")

except ValueError:
    print("Invalid Error")