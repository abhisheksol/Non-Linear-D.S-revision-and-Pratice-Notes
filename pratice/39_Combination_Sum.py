
def combination(index,target,res,data):
    if target==0:
        print(res[:])
    if index<len(data):
        if target>=data[index]:
            res.append(data[index])
            combination(index,target-data[index],res,data)

            res.pop()
            combination(index+1,target,res,data)





res=[]
combination(0,11,res,[8,7,4,3])

