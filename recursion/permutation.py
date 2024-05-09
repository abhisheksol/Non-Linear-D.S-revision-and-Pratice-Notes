def swap(char,i,j):
    temp=char[i]
    char[i]=char[j]
    char[j]=temp

def permutation(char,current_index,res):
    if current_index==len(char):
        res.append("".join(char))
        
    for i in range(current_index,len(char)):
        swap(char,i,current_index)
        permutation(char,i+1,res)
        swap(char,i,current_index)

def find_permutation(char):
    if char is None:
        return
    res=[]
    permutation(list(char),0,res)
    print(res)

print(find_permutation("ABCD"))