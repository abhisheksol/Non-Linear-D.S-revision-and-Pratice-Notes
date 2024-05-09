
col=[]
# column for loop
for i in range(3):
    # row
    row=[]
    for j in range(2):
        inp=int(input(f"enter the No for {i},{j} :"))
        row.append(inp)
    col.append(row)

print(col)    
print(col[2][0])

