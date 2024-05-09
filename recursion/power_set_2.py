# now power set should be unique 
# means no dublicate data should be present

def find_power_set(inp,out,filters):
    
    if len(inp)==0:
        print(out)
        if out  not in filters:
            filters.append(out)
        return 
    
    left_out=out
    right_out=out+inp[0]

    find_power_set(inp[1:],left_out,filters)
    find_power_set(inp[1:],right_out,filters)
    

    
  


filters=[]
find_power_set("abb","",filters)
print(filters)
