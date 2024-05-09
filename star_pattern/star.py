
n=6
print("pramid pattern")
for i in range(1,n):
    print(" "*(n-i)+"* "*i)

print("simple pattern \n ")

for j in range(1,n):
    print(" * "*j)

print("simple pattern reverse \n ")
            #  6 0 -1=> 6 5 4 3 2 1
for i in range(n,0,-1):
    print(" *"*i)

print("combination \n")
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)

