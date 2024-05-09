a=[
    ("mumbai","pune"),
    ("mumbai","solapur"),
    ("pune","solapur"),
    ("kholapur","pune"),
    ("solapur","kholapur"),  
   ]

dict={}

for start,end in a:
    # print(f"{start}:{end}")
    if start in dict:
        dict[start].append(end)
    else:
        dict[start]=[end]

print(dict)

