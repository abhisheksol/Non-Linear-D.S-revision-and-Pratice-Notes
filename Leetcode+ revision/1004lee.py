# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

nums = [1,1,1,0,0,0,1,1,1,1,0]
k=2
count=0
max_w=0
l=0
for r in range(len(nums)):
    if nums[r]==0:
        count+=1

    while count>k:
        if nums[l]==0:
          count-=1
        l+=1
        
    max_w=max(max_w,r-l+1)
        
    
print(max_w)





