#remove duplicates from the list
numbers = [1,2,2,2,3,3,4,4,5,5,6,6,7,7,8,9,10]
duplicate = []

for num in numbers:
    if num not in duplicate:
        duplicate.append(num)

print(duplicate)