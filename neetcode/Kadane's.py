nums = [-1,-3]

# prev_sum=nums[0]
# curr_sum=nums[0]

# for i in range(1,len(nums)):
#     curr_sum=max(nums[i],curr_sum+nums[i])
#     prev_sum=max(prev_sum,curr_sum)

# print(prev_sum)


current_sum=0
max_sum=float('-inf')

for i in range(len(nums)):
    current_sum+=nums[i]
    max_sum=max(max_sum,current_sum)

    if current_sum<0:
        current_sum=0
print(max_sum)




