#创建数据库，验证用户是否存在
users = [{"name" : "mia", "password" : "123", "status" : True },
        {"name" : "yancy", "password" : "456", "status" : True },
        {"name" : "Yolo", "password" : "789", "status" : False },
        ]
flag = 0
for j in range(3):
    user = input("请输入你的用户名：")
    pwd = input("请输入你的密码：")
    for i in users:
        if user == i["name"]:

            if pwd == i["password"] :
                if i["status"] == True:
                    print('登入成功！！！')
                    flag = 1
                    break
                elif i["status"] == False:
                    print('你以进入黑名单，无法登入。')
            else :
                print('你的密码错误')
            break
    else:
        print('你输入的用户名错误。')
    if flag :
        break






