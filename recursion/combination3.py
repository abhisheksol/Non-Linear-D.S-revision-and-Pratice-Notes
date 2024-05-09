# def combination(target,k,ds,index):
#     ans=[]
#     if ds is None:
#         ds=[]
#     if target==0 and k==0:
#         # ans.append(ds[:])
#         print(ds[:])
#     if k !=0:
#         for i in range(index,10):
#            ds.append(i)
#            combination(target-i,k-1,ds,index+1)
#            ds.pop()
    

# target=9
# k=3
# ds=[]
# combination(target,k,ds,1)


def combination(target,k,ds,index):
   
    if ds is None:
        ds=[]
    if target==0 and k==0:
        
        print(ds[:])
    if k !=0: 
        for i in range(index,10):
          if i not in ds:
             ds.append(i)
             combination(target-i,k-1,ds,i+1)
             ds.pop()

    

target=9
k=3
ds=[]
combination(target,k,ds,1)