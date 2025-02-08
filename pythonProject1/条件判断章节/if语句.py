# age = input("请输入你的年龄：")
# age = int(age)
# if age >=18:
#     print("huanyiguanl")
#     print("你可以进入网吧，请前往前台开机")
# elif age <=18:
#     print("未成年禁止进入网吧！！！")
#     print("请离开网吧！！！")
hight = input("请输入你的身高（单位：米）：")
hight = float(hight)
weight = input("请输入你的体重（单位：千克）：")
weight = float(weight)
BMI = weight / (hight**2)
print(BMI)
if BMI >= 23.9:
    print("过胖")
elif BMI < 23.9 and BMI >= 18.5:
    print("正常")
elif BMI < 18.5:
    print("过瘦")