n = input()
a = 0
b = 0
count = 0
coin = map(int, input().split(" "))
sortedCoin = sorted(coin)
for i in range(len(sortedCoin)):
    count += 1
    a += sortedCoin.pop()
    b = sum(sortedCoin)
    if b < a:
        break
    

# print(a)
# print(b)
print(count)