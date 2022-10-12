#  Find the maximum value to achive the current_capacity ...


def Maxcap(a,c):
    a.sort(key = lambda x : x[1]/x[0] ,reverse =True)
    curr_cap = c
    res = 0
    for j in range(len(a)):
        if a[j][0] <= curr_cap:
            curr_cap-=a[j][0]
            res = res+a[j][1]
        else:
            res+=a[j][1]*(curr_cap/a[j][0])
    return res

Activities = [[30,120],[20,100],[10,60]]

print(Maxcap(Activities,50))



# MTEHOD -II

#  Find the maximum value to achive the current_capacity ...

# class item:
#     def __init__(self, weight, value):
#         self.weight = weight
#         self.value = value

# def Maxcap(a,c):
#     a.sort(key = lambda x : x.value/x.weight ,reverse =True)
#     curr_cap = c
#     res = 0
#     for j in (a):
#         if j.weight <= curr_cap:
#             curr_cap-=j.weight
#             res = res+j.value
#         else:
#             res+=j.value*(curr_cap/j.weight)
#     return res

# Activities = [item(10,200),item(5,50),item(20,100)]
# # print(Activities)
# print(Maxcap(Activities,15))