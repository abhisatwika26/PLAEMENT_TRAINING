l1 = [2,3,4,3,2,5,5]
mapp = dict()

for i in l1:
    if i in mapp:
        mapp[i] += 1
    else:
        mapp[i] = 1

for key, value in mapp.items():
    if value == 1:
        print(key)
#bit manipulation
def xor(l1):
    s = 0
    for i in l1:
        s = s ^ i
    print(s)
xor(l1)

print(5 & 2)
print(5 << 1)
print(14 << 3)
print(178 << 13)

def check_even_odd(n):
    if n & 1 == 0:
        print("even")
    else:
        print("odd")


def even_odd(n):
    if n | 1 == n:
        print("odd")
    else:
        print("even")
n = int(input())
even_odd(n)

def even_odd(n):
    if bin(n ^ 1)[-1] == '0':
        print("odd")
    else:
        print("even")
even_odd(int(input()))

#xor sum 
def xorr(n):
  if (n % 4 == 1):
    return 1
  elif (n % 4 == 2):
    return (n + 1)
  elif (n % 4 == 3):
    return 0
  else:
    return n

n,m = map(int,input().split())
res = xorr(m) ^ xorr(n - 1)
print(res)

# o (1) time
def power_of_2(n):
  if n & (n - 1) == 0:
    return True
  else:
    return False
print(power_of_2(16))

#o(logn) time
n = 12
i = 0
while 1:
  if 2 ** i == n:
    print("yes")
    break
  if n < 2 ** i:
    print("no")
    break
  i += 1
bits = [1,1,0]
res = bits[-2:]
print(res)
