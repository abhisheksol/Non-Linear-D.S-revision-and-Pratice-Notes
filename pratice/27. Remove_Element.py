nums = [0,1,2,2,3,0,4,2]
val = 2

# res=[]
# count=0
# for i in nums:
#     if i==val:
#         count+=1
#     else:
#         res.append(i)

# for j in range(count):
#     res.append("_")
k = 0
for i in range(len(nums)):
    if nums[i] != val:
        nums[k] = nums[i]
        k += 1

print(k)
# print(count)