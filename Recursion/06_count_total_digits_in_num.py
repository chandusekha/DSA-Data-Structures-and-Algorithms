def countNum(N):
    if N==0:
        return 0
    return countNum(N//10)+1

print(countNum(999))