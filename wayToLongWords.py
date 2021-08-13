b = []
for _ in range(int(input())):
    word = input()
    if len(word) <= 10:
        b.append(word)
    else: 
        b.append(word[0] + str(len(word)-2) + word[-1])

for word in b:
    print(word)

