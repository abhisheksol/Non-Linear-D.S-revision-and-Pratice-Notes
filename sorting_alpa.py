a=[1,4,2,4,5]
temp=0
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp

print(a)

