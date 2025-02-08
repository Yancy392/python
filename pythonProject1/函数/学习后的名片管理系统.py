import email

print("*"*27)
print('''欢迎使用【名片管理系统】V1.0
    1.新建名片
    2.显示全部
    3.查询名片
    0.退出系统''')
print("*"*27)
cards=[{'name':'Yancy','phone':'131','QQ':'231','email':'231@QQ.com'},
       {'name':'mia','phone':'234','QQ':'232','email':'232@QQ.com'}]
def new_card():
    user={'name':name,'phone':phone,'QQ':qq,'email':email}
    cards.append(user)
    return True

def show_card():
    for card in cards:
        print(card)
    return True
def check_card(kw):
    for card in cards:
        for k,v in card.items():
            if kw == v:
                return card
def modify_card(result):
    result['name']=input('请输入改后的姓名：')
    result['phone'] = input('请输入改后的电话号码：')
    result['QQ'] = input('请输入改后的QQ号：')
    result['email'] = input('请输入改后的email：')
    return result
while True:
    op1 = input('请输入所需操作前的序号：')
    if op1 == '1':
        name = input('请输入你的名字：')
        phone = input('请输入你的电话号码：')
        qq = input('请输入你的QQ号：')
        email=input('请输入你的邮箱：')
        new_card()
        print('新建成功！')
    elif op1 == '2':
        show_card()
    elif op1 == '3':
        kw = input('请输入你查的关键字：')
        result=check_card(kw)
        if result:
            print(result)
        else:
            print('没有查到相关信息,请重试！！！')
        op2= input('如果想修改请输入4，删除输入5：')
        if op2 == '4':
            result2=modify_card(result)
            print(result2)

        elif op2 == '5':
            cards.remove(check_card(kw))
        else:
            print('请按要求输入')

    elif op1 == '0':
        print('你已退出系统，欢迎下次光临')
        break
    else:
        print('请正确输入')