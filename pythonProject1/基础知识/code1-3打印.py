year=2024
mouth=1
day=9
week="四"
weather="阴"
temp=7.5
print("我是桂冬羊")

print (year, '年，我要好好学python',sep='')# sep:设置打印多个内容的分隔符
print(end='\n')# \n为空行符，表示空格意思
print(year, '年,我要好好练习口语',sep='',end='\n\n')# 句内空行
print(year, '年,我要好好赚钱',sep='')
print("今天是 %d 年 %d 月 %d 日,星期 %s，%s,气温 %.1f" % (year,mouth,day,week,weather,temp))
