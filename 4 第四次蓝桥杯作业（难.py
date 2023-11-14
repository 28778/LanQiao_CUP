li = []  # 初始化一个存储数字的列表。
'''
|------------------------------------|
|  def  | 函数名  |       释义       |
|-------+---------+------------------+
| def x | find_z  | 找到存在质数的数 |
| def y | find_3  | 找到存在3的数    |
| def z | find_33 | 找到33合体的数   |
|------------------------------------|
'''

'''
开始定义各个公式↓
'''


# 判断是否质数，如果是，就返回数字本身。
def x(number):
    if number <= 1:  # 判断数字是否小于等于1
        return None  # 不成立
    for i_ in range(2, int(number ** 0.5) + 1):  # 遍历2~该数值
        if number % i_ == 0:  # 判断质数
            return None  # 不成立
    return number  # 成立


# 判断一个数是否包含3，如果是，就返回数字本身。
def y(number):
    if '3' in number:
        return number


# 判断3是否是连续的，如果是，就返回数字本身。
def z(number):
    if '33' in number:
        return number


'''
正式开始运算↓
'''

# 第一轮：存在3的数字。
for i in range(1, 1000000):  # ←←←更改这个数就可以了←←←
    find_3 = y(str(i))  # 在1-1000中，找存在3的数字
    if find_3 is not None:  # 去掉None
        li.append(find_3)  # 加到列表里

        # 第二轮：找质数并添加*
        find_z = x(int(find_3))  # 在存在3的数字里，找质数
        if find_z is not None:  # 去掉None
            index = li.index(find_3)  # 在li里寻找对应的索引，用于找到被替换的数字（find_3）
            li[index] = f"{find_z}*"  # 替换掉符合“质数”的数（加*符号）

        # 第三轮：找33并添加&
        find_33 = z(find_3)  # 运行函数z，在数字3里找符合33连续的（包括333）
        if find_33 is not None:  # 去掉None
            try:  # 先尝试这个代码（因为避免它找不到对应的数而报错）
                index = li.index(find_33)  # 同样，寻找索引，然后替换
                li[index] = f"&{find_33}*"
            except ValueError:  # 如果报错ValueError，再尝试这个代码
                index = li.index(f"{find_33}*")  # 同样，寻找索引，然后替换
                li[index] = f"&{find_33}"

# 已经实现了
print(','.join(map(str, li)))