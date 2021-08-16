n = int(input())
count = 0
for i in range(n):
    stud = list(map(int, input().split(" ")))
    if stud.count(1) >= 2:
        count += 1

print(count)