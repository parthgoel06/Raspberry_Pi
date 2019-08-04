a = []
a = input()
lower = []
upper = []
odd = []
even = []

for i in range (len(a)):
    if (a[i].isalpha()):
       if(a[i].isupper()):
           upper.append(a[i])
       else:
            lower.append(a[i])
    elif (int(a[i])%2==0):
        even.append(a[i])
    else:
        odd.append(a[i])

upper.sort()
lower.sort()
even.sort()
odd.sort()         

b = lower+upper+odd+even
print(*b,sep='')
