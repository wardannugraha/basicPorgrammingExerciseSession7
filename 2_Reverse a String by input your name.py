# Input name
name = input ("Enter Your Name : ")

# empty string to store the reversed name
Reversed_name = ""

# reverse name and appending to an empty string
for i in range(len(name)-1, -1, -1) :
    Reversed_name += name[i]

# print reverse name
print("Reversed Name :", Reversed_name)