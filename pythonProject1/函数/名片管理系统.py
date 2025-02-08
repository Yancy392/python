print("*"*27)
print()
print('欢迎使用【名片管理系统】V1.0')
print('1.新建名片')
print('2.显示全部')
print('3.查询名片')
print('0.退出系统')
print("*"*27)
a = input('请输入功能前方的数字来使用功能：')
a = int(a)
print(a)
users = {'Yancy':{'姓名':'Yancy','电话':131,'QQ':231,'邮箱':'231@QQ.com'},
         'mia':{'姓名':'mia','电话':234,'QQ':232,'邮箱':'232@QQ.com'},}
if a == 1:
    name1 =input('请输入你的名字：')
    payphone=input('请输入你的电话号码：')
    QQ号=input('请输入你的QQ号')
    EM=input('请输入你的邮箱')
    users[name1] = {'姓名':name1,'电话':int(payphone),'QQ':int(QQ号),'邮箱':EM}
    print('新建成功！！')
    for k,v in users.items():
        print(k,v)
elif a == 2:
    for k,v in users.items():
        print(k,v)
elif a == 3:
    user = filter(lambda x:x==input('请输入你想查名片的姓名：'),users)
    print(list(user))
elif a == 0:
    print('你已退出系统，欢迎下次光临！！！')

