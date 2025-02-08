num1 = 10#（不可变数据）#全局变量
list1 = [1,2,3,4,5]
def f():
    global num1
    list1[2] = 8
    num1 = 20#局部变量
    num2 = 20
    print(num1, num2)
    print(list1)
f()
print('函数外的num1:', num1)
print('函数外的list1:', list1)