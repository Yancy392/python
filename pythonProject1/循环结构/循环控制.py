#break
n = 10
a = 2
while a<n:
    if n%a==0:
        print(n,"不是一个质数")
        break

    else:
        print(n,"是一个质数")
        break
    a += 1



n = 10
a = 2
flag = 0
while a<n:
    if n%a==0:
        print(n,"不是一个质数")
        flag = 1
        break
    a += 1
if flag == 0:
    print(n,"是一个质数")


n = 10
a = 2
while a<n:
    if n%a==0:
        print(n,"不是一个质数")
        break
        a += 1

else:
    print(n,"是一个质数")



n = 11
flag = 0
for a in range(2,n):
    if n%a==0:
        print(n,"不是一个质数")
        flag = 1
        break
if flag == 0:
    print(n,"是一个质数")


