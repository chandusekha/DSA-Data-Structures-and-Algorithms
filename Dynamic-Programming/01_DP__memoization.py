# fabinacii series of n

memo = [-1 for i in range(100)]
def fab(n):
    if n<=1:
        return n
    if memo[n] != -1:
        return memo[n]    
    else:
        memo[n]= fab(n-1)+fab(n-2)
        return memo[n]
print(fab(4))


# Method - II


# memo = [-1 for i in range(100)]
# def fab(n):
#     if memo[n] == -1:
#         if n<=1:
#             return n
#         else:
#             memo[n] = fab(n-1)+fab(n-2)
#             return memo[n]
#     else:
#         return memo[n]


# # n = int(input('enter the N value : '))
# print(fab(4))