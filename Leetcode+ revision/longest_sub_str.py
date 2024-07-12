s = "pwwkew"

sets=set()
max_w=0
l=0
for r in range(len(s)):
    while s[r] in sets:
        sets.remove(s[l])
        l+=1
    
    w=r-l+1
    max_w=max(max_w,w)
    sets.add(s[r])
print(max_w)
    




