def comb(ip,op):
    if len(ip)==0:
        print(op)
        return
    
    op1=op
    op2=op1+str(ip[0])

    comb(ip[1:],op2)
    comb(ip[1:],op1)



comb([1,2,3],"")
