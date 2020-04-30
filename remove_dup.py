numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
new = []

count= len(numbers)

for i in numbers:
    uniques.append(numbers.count(i))
   
print(uniques)

count_a = len(uniques)

for j in range(0,count_a,1):
    if uniques[j]==1:
        new.append(numbers[j])



print(new)




    
    