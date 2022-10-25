
def SumOfDigits(N):
    if N<10:
        return N
    return SumOfDigits(N//10)+N%10
print(SumOfDigits(99999))