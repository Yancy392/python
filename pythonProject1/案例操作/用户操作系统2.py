users = {'mia' : {"name" : "mia", "password" : "123", "status" : True },
        'yancy' :{"name" : "yancy", "password" : "456", "status" : True },
        'Yolo': {"name" : "Yolo", "password" : "789", "status" : False },
         }
for j in range(3):
    user = input("请输入你的用户名：")
    pwd = input("请输入你的密码：")
    if user in users and pwd ==users[user]['password'] and users[user] == True:
        print('登入成功！')
        break
    elif user in users  and not users[user]["status"] :
        print('heihu')
    elif user in users and pwd != users[user]['password']:
        print('密码错误！')
    else:
        print('用户名错误')
