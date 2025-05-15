def is_prime(n):
    if n == 2 or n == 3:
        return True
    flag = 0
    for i in range(2,n//2 + 1):
        if n % i == 0:
            flag = 1
            break
    if flag == 1 or n == 1:
        return False
    return True
def main_func(n):
    if is_prime(n) == True:
        if n > 200:
            print("prime greater than 200")
        else:
            print("prime not greater than 200")
    else:
        print("not a prime")
n = int(input())
main_func(n)
