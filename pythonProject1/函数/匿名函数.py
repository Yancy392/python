#map 映射函数
a = [1,2,3,4,5,6]
b = map(lambda x: x ** 2, a)#map(f,a)即将a中所有元素一一映射为新列表（通过函数f）
print(list(b))
#普通解法
b = []
for i in a:

    b.append(i**2)
print(b)
#reduce 累积函数（累乘，累加……）
from functools import reduce
b = reduce(lambda x,y:x*10+y,a)
print(b)
#filter 过滤函数
b = filter(lambda x: x%2==0,a)
print(list(b))