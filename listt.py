def summ(n):
    if n == 0:
        return 0
    return n + summ(n-1)
n = int(input())
print(summ(n))


        
    
