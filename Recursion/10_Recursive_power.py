def RecursivePower(n,p):
        if p==0:
            return 1
        return RecursivePower(n,p-1)*n
print(RecursivePower(2,9))

