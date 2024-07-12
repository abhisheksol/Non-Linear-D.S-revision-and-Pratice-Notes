nums = [-4,-2,1,-1,4,8]

close=nums[0]
for i in nums:
    if abs(i)<abs(close):
        close=i

if close <0 and abs(close) in nums:
    print("yes")
else:
    print("no only one")
print(close)

    
