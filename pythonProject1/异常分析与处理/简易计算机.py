while True:
    try:
        op = input("请输入需运算算式：")
        if "+" in op:
            a = op.split("+")
            result = int(a[0]) + int(a[1])
            print(result)
        elif"*" in op:
            a = op.split("*")
            result = int(a[0]) * int(a[1])
            print(result)
        elif"-" in op:
            a = op.split("-")
            result = int(a[0]) - int(a[1])
            print(result)
        elif"/" in op:
            a = op.split("/")
            result = int(a[0]) / int(a[1])
            print(result)
        elif op == "C":
            print("您已退出计算机！")
            break
        else:
            raise Exception("请按照格式输入，如1+2")
    except ZeroDivisionError:
        print("除数不能为零！")
    except Exception as e:
        print(e)

