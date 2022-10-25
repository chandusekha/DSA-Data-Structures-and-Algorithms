def TOH(n,fr,to,ax):
    if n<1:
        return
    TOH(n-1,fr,ax,to)
    print(n ,"is moved from " , fr, " to ", to)
    TOH(n-1,ax,to,fr)
n = 4
TOH(n,'a','c','b')