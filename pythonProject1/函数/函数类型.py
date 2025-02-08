# #函数
# def square(x,y):
#     return x*y
# a =int(input('请输入需求图形面积的长：'))
# b =int(input('请输入需求图形面积的宽：'))
# c = square(a,b)
# print(c)
# #默认函数
# def main(a,n=18):
#     return'Yancy,height:%d,age:%d'%(a,n)
# a = main(170)
# print(a)
#可变函数
#计算数列的平方和
def total(*a):
    print(a)
    a = list(a)
    result = 0
    for i in a:
        result += i**2
    return result#这个放到循环外
result=total(1,2,3)
print(result)
