a=[2,90,10,-4,21,7]

k=3
sum=0
msum=0
for i in range(0,k):
    # print(a[i])
    sum+=a[i]
    msum=sum

# elimanate the first charater by i-k(3-3) to len

for i in range(k,len(a)):
    a_val=a[i-k]
    sum=sum-a[i-k]+a[i]
    msum=max(sum,msum)

print(msum)