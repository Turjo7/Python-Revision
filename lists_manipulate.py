numbers=[1,2,3,4,5,6,7,8,9,10,11]
numbers.append(12)
print(numbers)
numbers.insert(3,20)
print(numbers)
numbers.remove(10)
print(numbers)

print(numbers.pop())
print(numbers.index(7))
print(50 in numbers)
print(numbers.count(7))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers_1 = numbers.copy()
print(numbers)


numbers.clear()
print(numbers)