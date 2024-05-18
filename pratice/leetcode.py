s="-+12"
s=s.strip()
res=0
set_negative=False

if s[0]=="-":
    set_negative=True
    s=s[1:]
    
if s[0]=="+":
    s=s[1:]
        
# ------------------------------------------------------

for i in s:
    
    if i.isnumeric():
        res=res*10+int(i)
    elif i==" ":
        pass
    else:
        break
  

        

# ---------------------------------------------------
if set_negative is True:
    print(-res)
else:
    print(res)


