string = input()
lower = 0
upper = 0
for letter in string:
    if letter.isupper():
        upper += 1
    else: 
        lower += 1

if upper > lower:
    print(string.upper())
else: 
    print(string.lower())
