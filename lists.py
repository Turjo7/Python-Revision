names=['Turjo','Billu','Meaw']
print(names)
names[-1]="Kochi"
print(names)

numbers=[10,8,3,60,5,4,0,-2]
a=numbers[0]
b=(len(numbers))

for i in range(0,b,1) :
    if numbers[i]>=a:
        a=numbers[i]


print(f'The Biggest Number: {a}')


matrix= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix)
print(matrix[0])
print(matrix[0][1])
print(matrix[1][1])
print(matrix[2][1])

print("--------------------------------------------------------")

for row in matrix:
    for item in row:
        print(item)