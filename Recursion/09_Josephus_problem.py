def josephus(n,k):
        #Your code here
        if n == 1:
            return n
        return (josephus(n-1,k)+k-1)%n+1
print(josephus(7,3))