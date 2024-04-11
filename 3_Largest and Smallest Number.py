#numbers
numbers = [10, 20, 5, 40, 30, 72, 34]

# initialize variables to hold the largest and smallest number
largest = numbers [0]
smallest = numbers [0]

# iterate through and update the list
for num in numbers :
    if num > largest :
        largest = num
    elif num < smallest :
        smallest = num

# print largest and smallest number
print("Largest number is : ", largest)
print("Smallest number is : ", smallest)