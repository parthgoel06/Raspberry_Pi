n = int(input("enter the size of list"))
ls = []
ls2 = []
for i in range(n):
    ls.append(int(input()))
print(ls)
for i in range(n):
    a = 1
    for j in range(n):
        if i==j:
            continue
        else:
            a *= ls[j]
    ls2.append(a)
print(ls2)     
