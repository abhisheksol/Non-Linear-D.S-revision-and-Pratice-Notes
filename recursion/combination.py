def combination(index,target,data,ds):
  if ds is None:
    ds=[]
  if target==0:
    print(ds[:])
  if index<len(data):
    if target>=data[index]:
      ds.append(data[index])

      combination(index,target-data[index],data,ds)
      # backtrack when it reaches the left side leaf node
    #     ()
    #    /
    #   /
    #  /   bcs we have to go for right \  we will do this by elementating last element form ds[1,2,pop]
    # ()                                \
                            #            \
                        #                ()
      ds.pop()
      combination(index+1,target,data,ds)


arr = [2, 3, 6, 7]
ds = []
result = combination(0, 7, arr, ds)
print(result)