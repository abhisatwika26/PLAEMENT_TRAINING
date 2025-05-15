import sys
sys.setrecursionlimit(3000) # by setting a limit for rescurive calls recursion depth can be changed
def qwer(x):
    print("hi",x)
    qwer(x+1)
qwer(1)

# recursion depth in java , c ++ depends on compiler - complier design
#in python at max 1000 recursive calls can be made
#difference between recusrion and while loop is that while loop in oython is set for infinity
#so when we write while(1) : print("hi") hi is perinted infinie times but in recursion it only runs based on the recursion limit - error : maximum recursion depth exceeded
#stack is overflown in recursion

def qwer(x):
    if x == 6:
        return
    print("hi",x)
    qwer(x+1)
    print("hi",x)
qwer(1)
print("hello")

def sum_even(x,i):
    if len(x) == i:
        return 0
    if x[i] % 2 == 0:
        return x[i] + sum_even(x,i+1)
    else:
        return sum_even(x,i+1)
a = [2,5,6,7,1,4,3,6]
print(sum_even(a,0))

def sum_even(x):
    if len(x) == 0:
        return 0
    if x[0] % 2 == 0:
        return x[0] + sum_even(x[1:])
    return sum_even(x[1:])
a = [2,5,6,7,1,4,3,6]
print(sum_even(a))

def reverse(n,re = 0):
    if n == 0:
        return re
    return reverse(n//10,re* 10 + n % 10)
print(reverse(12345))

def check_prime(n, i=2):
    if n <=1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return check_prime(n,i+1)

def prime(lst, c=0):
    if len(lst) == 0:
        return c
    if check_prime(lst[0]):
        return prime(lst[1:], c+1)
    else:
        return prime(lst[1:], c)

a = [3, 5, 7, 11]
print(prime(a))


def pos(n):
    i = 3
    f = 0
    while 1:
        n -= i
        if n == 1:
            f = 1
            break
        elif n < 1:
            break
    if f == 1:
       return True
    return False
print(pos(20))

def qwer(x,n,m,c = 0):
    if x == 1:
        return True,c 
    if x < 1:
        return False 
    return qwer(x-n,n,m,c+1) or qwer(x-m,n,m,c+1)
print(qwer(10,3,5))

def dfs_approach(x,n,m):
    visited = set()
    q = []
    q.append(x)
    visited.add(x)
    while q:
        i = q.pop(0)
