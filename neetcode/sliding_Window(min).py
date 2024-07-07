#  target = 4, nums = [1,4,4]
nums = [2,3,1,2,4,3]
# nums = [1,4,4]
target = 7
l=0
min_len=float('inf')
curr_sum=0
for r in range(len(nums)):
    curr_sum+=nums[r]

    while curr_sum>=target:
        min_len=min(min_len,r-l+1)
        curr_sum-=nums[l]
        l += 1
# If min_len was never updated, it means no subarray curr_sums to the target
if min_len == float('inf'):
    min_len = 0

print(min_len)

