def toh( N, fromm, to, aux):
        if N==0:
            return
        toh(N-1,fromm,aux,to)
        print("move disk", N ,"from rod", fromm,"to rod",to)
        toh(N-1,aux,to,fromm)

        return ((2**N)-1)
print(toh(3,1,3,2))