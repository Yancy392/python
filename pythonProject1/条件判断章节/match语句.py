x = input("请输入一个数字")
x = int(x)
match x:
    case 1:
        print(111)
    case 2:
        print(222)
    case 3:
        print(333)
    case 4:
        print(444)
    case _:
        print("加载已超时")