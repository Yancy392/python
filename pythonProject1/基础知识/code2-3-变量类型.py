N1 = 5.559
N2 = 14.28
print(N1+N2)
print(round(N1+N2,2))#四舍五入round
#向上取整 ceil
import math #数学库
print(math.ceil(N1+N2))
import math
print(math.floor(N1+N2))#floor 向下取整
#字符串索取

number = '123456789'
print(number[0])
print(number[-1])
print(number[0:8:1])
print(number[::2])
print(number[::-1])
print(number[-1:-10:-1])
s = 2
print(bool(s))
f = 0.5
print(bool(f))
b = '10'
print(int(b,16))
#转义字符(只需转义相同符号）
print("你好’\",你真漂亮")
