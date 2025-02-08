price = 10.5
quantity = input("请输入你想购买的数量(单位斤）：")
quantity = float(quantity)
money = price * quantity
print("你所需支付的金额为:",money)
print(type(money),isinstance(price,int))