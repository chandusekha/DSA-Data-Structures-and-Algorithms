def printNos(N):
        if N < 1:
            return 1
            
        printNos(N-1)
        print(N,end=" ")

printNos(10)