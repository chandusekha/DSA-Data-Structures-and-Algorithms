def digit_root(N):
    if N<10:
        return N

    sum = digit_root(N//10)+N%10
    return digit_root(sum//10)+sum%10
print(digit_root(99999))