x=-123
a=str(x)

final_str=""
if x <0:
    final_str="-"
for i in range(1,len(a)+1):
    final_str+=a[-i]
    # print(a[-i])

if final_str[-1] == "-":
    final_str = final_str[:-1]


data=int(final_str)
# if -2**31<=data<=2**31:
if data in range(-2**31,2**31-1):
    print("True")
else:
    print("False")
print(data)


