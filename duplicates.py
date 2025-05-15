mapp = dict()
lis = [2,3,4,2,5,6,7,8,6,7,5]
for i in lis:
    if i in mapp:
        mapp[i] += 1
    else:
        mapp[i] = 1
lis2 = list(mapp)
print(lis2)
