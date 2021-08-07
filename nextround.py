n = list(map(int, input().split(" ")))
sec_num = list(map(int, input().split(" ")))
count = 0
checkAll = all(elem == sec_num[0] for elem in sec_num)
if checkAll and sec_num[0] > 0: 
    print(sec_num.count(sec_num[0]))
else: 
    for num in sec_num:
        if num > n[1]:
            count += 1
    print(count)

