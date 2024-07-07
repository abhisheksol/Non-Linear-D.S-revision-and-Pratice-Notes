prev_sum=nums[0]
curr_sum=nums[0]

for i in range(1,len(nums)):
    curr_sum=max(nums[i],curr_sum+nums[i])
    prev_sum=max(prev_sum,curr_sum)

print(prev_sum)