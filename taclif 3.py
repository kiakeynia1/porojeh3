a = []
while True:
    b = int(input())
    if b == 00:
        break
    a.append(b)
for i in range(1,len(a)):
    if a[i] < a[i-1]:
        print('no')
        exit()
else:
    print('yes')
