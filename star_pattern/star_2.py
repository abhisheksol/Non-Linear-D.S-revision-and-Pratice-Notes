n=3
for i in range(0,n+1):
    for j in range(0,i+1):
        print(" *",end=" ")
    print("")


for j in range(0,n+1):
    for i in range(0,j+1):
        print("# ",end=" ")
    print("")


# actual 
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
n=5
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
    
for i in range(n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
    
print()   
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()
    
print()

for i in range(n+1):
    for j in range(1,n-i):
        print(j, end=" ")
    print()

for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i+1):
        print(" * ", end=" ")
    print()
    
for i in range(n):
    for j in range(n-i):
        print(" ", end=" ")
    for i in range(i+1):
        print("*", end=" ")
    for j in range(i):
        print("*", end=" ")
    
    print()
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for i in range(n-i):
        print(".", end=" ")
    for j in range(i):
        print(".", end=" ")
    
    print()
    
