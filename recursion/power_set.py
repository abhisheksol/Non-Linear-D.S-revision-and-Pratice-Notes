def solve(ip,op):
    if len(ip)==0:
        print(op)
        return
    
    op1=op
    op2=op+str(ip[0])

    

    
    solve(ip[1:],op1)
    solve(ip[1:],op2)

solve([1,2],"")



# def solve(ip, op):
#     if len(ip) == 0:
#         print(op)
#         return

#     op1 = op
#     op2 = op + ip[0]

#     solve(ip[1:], op1)
#     solve(ip[1:], op2)

# # Example usage:
# solve("abc", "")



















# # def power_set_recursive(original_set, index, current_set, result):
# #     # Base case: add the current subset to the result
# #     result.append(current_set.copy())

# #     # Recursive case: generate subsets including and excluding the current element
# #     for i in range(index, len(original_set)):
# #         current_set.append(original_set[i])
# #         power_set_recursive(original_set, i + 1, current_set, result)
# #         current_set.pop()

# # # Function to get the power set of a set
# # def power_set(input_set):
# #     result = []
# #     power_set_recursive(input_set, 0, [], result)
# #     return result

# # # Example usage:
# # my_set = [1, 2]
# # resulting_power_set = power_set(my_set)
# # print("Power Set:", resulting_power_set)


# def generate_subsets(nums):
#     if not nums:
#         return [[]]
    
#     previous_subsets = generate_subsets(nums[:-1])
#     result = []
    
#     for subset in previous_subsets:
#         result.append(subset + [nums[-1]])
    
#     return previous_subsets + result

# # Example usage:
# nums_input = [1, 2]
# resulting_subsets = generate_subsets(nums_input)
# print("Subsets:", resulting_subsets)

