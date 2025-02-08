# for i in range(10):
#     print(i)
#     print("hello")
# result = 0
# for i in range(101):
#     result += i
# print(result)
#1！+2！+3！——n!之for


result2 =0
for n in range(5):
    if n > 0:
        result = 1
        for i in range(n+1):
            if i > 0:
                result *= i
        print(result)
        result2 += result
        print(result2)
        print("*"*20)
print(result2)
# n = 3
# result2 = 0
# for i in range(n+1):
#     if i > 0:
#         result=6
#         print(result)
#         result2 += result
#         print("*"*20)
#         print(result2)
print("-"*20)
n=1
result2=0

while n<5:
    result = 1
    i = 1
    while i<n+1:
        if i >0:
            result *= i
            i +=1
    print(result)
    result2 += result
    n +=1
print("*"*20)
print(result2)