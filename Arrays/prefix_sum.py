arr=[6,3,-2,4,-1,0,-5]

prefix_arr=[]
sum=0
for i in range(len(arr)):
    sum+=arr[i]
    prefix_arr.append(sum)

print(prefix_arr)



def prefix(num1,num2):

    if num1==0:
        data=prefix_arr[num2]
    else:
        data=prefix_arr[num2]-prefix_arr[num1-1]
    print(data)


prefix(2,3)