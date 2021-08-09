k, n, w = map(int, input().split(" "))
total = 0
borrow = 0
for i in range(w):
    total += k*(i+1)

borrow = total - n
if borrow > 0:
    print(borrow)
else:
    print(0)