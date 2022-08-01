# 电竞经理招聘推荐程序V1.1
# 运行时需要添加选手数据库

import one
import two
import three


print("电竞经理选手招聘助手V1.0")
print("1.1地区+4战队+1tag1+2tag2")
print("2.2位置+1地区+2tag1+3tag2")
print("3.1地区+4战队+3tag2")
a = int(input("选择类型："))
if a==1:
    one.one_a()
elif a==2:
    two.two_a()
else:
    three.three_a()