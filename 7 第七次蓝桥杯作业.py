# 模糊的单据

for i in range(25006, 25997):
    if i % 37 == 0 or i % 67 == 0:
        if i % 10 == 6:
            print(i)

# 用1、3、5、8这几个数字，能组成互不相同且无重复数字的三位数各是多少？总共有多少个？
num = 0
li = []
for i in range(135, 854):
    if "1" in str(i) and "3" in str(i) and "8" in str(i):
        li.append(i)
        num += 1
    if "1" in str(i) and "3" in str(i) and "5" in str(i):
        li.append(i)
        num += 1
    if "8" in str(i) and "3" in str(i) and "5" in str(i):
        li.append(i)
        num += 1
    if "8" in str(i) and "1" in str(i) and "5" in str(i):
        li.append(i)
        num += 1
li.sort()
for i in li:
    print(i)
print(num)





# 小明的电子邮箱密码忘记了，请你帮他找出密码。他零星记得密码的信息如下:
#
# 1 )密码是六位数字，前面两位是31 ;
#
# 2 )最后两位数字相同;
#
# 3 )能被16和46整除;
#
# 请你找出所有可能的密码并统计个数。
num = 0
for i in range(310000, 320000):
    if i % 10 == i // 10 % 10 and i % 16 == 0 and i % 46 == 0:
        num += 1
        print(i)
print(num)