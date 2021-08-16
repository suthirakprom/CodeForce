y = input()
z = 0


z = int(y) + 1
z = str(z)
while len(set(z)) != len(z):    # check if the character is unique or not
    z = int(z) + 1              # change it to int in order to increase
    z = str(z)                  # change it back to string in order to check the statement
print(z)



