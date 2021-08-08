string1 = input().upper()
string2 = input().upper()
count = 0
if string1 == string2:
    print("0")
else: 
    for i in range(len(string1)):
        if string1[i] < string2[i]:
            count = -1  
            break
        elif string1[i] > string2[i]: 
            count = 1
            break
        
            # 1
    print(count)