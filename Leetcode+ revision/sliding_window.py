a=[2,9,31,-4,21,7]

k=3
sum=0
msum=0
for i in range(0,k):
    sum+=a[i]

# elimanate the first charater by i-k(3-3) to len

for i in range(k,len(a)):
    sum=sum-a[i-k]+a[i]
    msum=max(sum,msum)

print(msum)