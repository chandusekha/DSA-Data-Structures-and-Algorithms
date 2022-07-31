
# head={
#     "value":10,
#     "next":{
#         "value":25,
#         "next":{
#             "value":35,
#             "next":{
#                 "value":45,
#                 "next":None
#             }
#         }   
#     }
# }
# print(head['next']['next']['value'])


class hashTabel:
    def __init__(self,size=7):
        self.get_map=[None]*7

t1=hashTabel()
t1.get_map