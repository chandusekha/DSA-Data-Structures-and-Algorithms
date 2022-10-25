
def power(N,R):
    #Your code here
    if R == 0:
        return 1
    temp = power(N, R//2)
    even = int(temp * temp) % 1000000007
    if R % 2 == 0:
        return even
    return int(even * N) % 1000000007  
 


ans = power(999,999)
print(ans)