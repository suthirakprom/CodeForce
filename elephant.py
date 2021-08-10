x = int(input())
res = 0
if x <= 5:
    print(1)
else:
    if x % 5 == 0:
        res = x // 5
        print(res)
    else: 
        res = (x // 5) + 1
        print(res)
    