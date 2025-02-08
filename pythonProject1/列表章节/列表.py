list2 = list("'12345'")
# print(list2)
# for i in list2:
#     print(i)
# for i, j in enumerate(list2):
#     print(i, j)
for i in range(0,len(list2)):
    print(i,list2[i])



#列表的常用方法  变量.方法（）
list2.append("666")#添加元素
print(list2)
list2.extend([1,1,3,4])#添加列表
print(list2)
list2.insert(2,'hello')#插入（索引空位，对象）
print(list2)
#删除
list2.remove('hello')#删除元素，删除前面的元素
print(list2)
list2.pop(7)#索引删除
print(list2)
#清空
list2.clear()
print(list2)
