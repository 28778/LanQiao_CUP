# 第一题 单词后缀处理
# 输入一个英语单词，若单词后缀为"er"、"ly"、"ing"，就删除后缀后再输出，否则原样输出。
# 输入样例1：lovely
# 输出样例1：love
# 输入样例2：singer
# 输出样例2：sing
# 输入样例3：working
# 输出样例3：work

word = input()
if word[-2:] == "ly":  # 使用字符串切片，将单词后两位拎出来比对，若是，即运行。
    word = word.replace("ly", "")  # 使用.replace方法，将"ly"替换为""
elif word[-2:] == "ng":
    word = word.replace("ing", "")
elif word[-2:] == "er":
    word = word.replace("er", "")
print(word)

# 第二题 贴门牌号
# 小蓝要为一条街的住户制作门牌号，这条街一共有2020位住户，门牌号从1到2020编号。小蓝制作门牌的
# 方法是先制作0到9这几个数字字符，最后根据需要将字符粘贴到门牌上，例如门牌1017需要依次粘贴字符
# 1、0、1、7，即需要1个字符0，2个字符1，1个字符7。请问要制作所有的1到2020号门牌，总共需要多少个字符2?
# 提示：不是问多少个数字里有2，而是总共有多少个“2”。（如2020这个数中就有2个“2”  ）
# 输出样例：624
# 先做门牌号，后统计号数
num = 0
for i in range(1, 2021):
    for j in str(i):
        if "2" in j:
            num += 1
print(num)

# 第三题 加密字符串
# 编程实现：
# 把输入的内容中全部字符加密,加密方法为：
# 1.所有英文字母变成数字(ascii)，
# 2.空格、换行符、数字和标点符号不变。
# 提示，判断是否为字母的方法：
# letter = 'a'
# if letter.isalpha():
#     print('this is a letter')
# 输入描述:字符串形式输入
# 输出描述:按规则加密后的内容，对应所有字母变成数字的加密版本。
# 输入样例：Better an empty purse than an empty head.
# 输出样例：66101116116101114 97110 101109112116121 112117114115101 11610497110 97110 101109112116121 10410197100.

word = input()
for i in word:
    if i.isalpha():  # 使用isalpha方法判定是否为字母
        i = ord(i)  # 使用ord转换为ascii码
        print(i, end="")
    else:
        print(i, end="")

# 第四题 字符类型统计
# 输入一行字符，分别统计出其英文字母、空格、数字和其它字符的个数并输出。
# 输入描述：输入一行字符
# 输出描述：按英文字母、空格、数字和其它字符的顺序输出其对应的个数
# 输入样例：
# a1 b2 c d4 !!! 5
# 输出样例：
# 4 英文字母
# 5 空格
# 4 数字
# 3 其他

eng, space, number, other = 0, 0, 0, 0
word = input()
for i in word:
    if i == " ":
        space += 1
    elif i.isdigit():
        number += 1
    elif i.isalpha():
        eng += 1
    else:
        other += 1
print(f"{eng} 英文字母\n{space} 空格\n{number} 数字\n{other} 其他")

# 第五题 寻找回文数
# 编程实现：求不同位数的回文数的个数。
# 用户输入要求几位数（3-6 位）的回文数的个数，程序输出有多少个回文数，并输出所有含有数字 99 的回文数。
# 输入描述：要求几位数的回文数的个数
# 输出描述：几位数中含有数字 99 的回文数
# 输入样例1：
# 3
# 输出样例1：
# 999
# 3 位数的回文数有 90 个。
# 输入样例2：
# 4
# 输出样例2：
# 1991 2992 3993 4994 5995 6996 7997 8998 9999
# 4 位数的回文数有 90 个。
j = 0  # 初始化计数j
word = int(input())
word_num = word * "9"
for i in range(1, int(word_num)+1):
    i = str(i)
    # if语句开始
    if len(i) >= word:  # 首先剔除比用户输入位数小的数
        # 判断开始
        if i[0] == i[-1]:  # 判断是否回数 step 1
            if i[1] == i[-2]:  # 判断是否回数 step 2
                if i[2] == i[-3]:  # 判断是否回数 step 3
                    if "99" in i:  # 判断有99的数
                        print(i, end=" ")
                    j += 1
print(f"\n{word} 位数的回文数有 {j} 个。")


# 第六题 判断幸运号码

# 提示信息：
# 我国固定电话号码由区号和 8 位数字组成，中间用"-"号分隔，例如：0573-82651630，其中：
# 1）"-"号前是地区代码，由 3-4 位数字组成，如北京是 010、上海是 021、浙江是 0573；
# 2）"-"号后是 8 位数字组成的电话号码。
#
# 【编程实现】
# 某电视台要从拨打热线电话的观众中选取一批幸运观众，请你按标准格式输入一个电话号码，并根据以下规则判断是否是幸运号码，幸运号码必须满足以下 4 个条件（按优先顺序排列）：
#
# 1）用户来自北京地区；
# 2）电话号码（后 8 位数字）中含数字“8”；
# 3）电话号码是偶数；
# 4）电话号码能被3整除。
# 输入描述: 一些数字
# 0573-82651630

# 010 66781232
# 010-66781232 不是幸运号码
# 010-66781232 不能被3整数
cause = []
tele_num = input()
tele_num_ = tele_num.replace("-", " ")  # 进行这一步，使用replace将-替换为空格。方便最后的打印
tele_num__ = tele_num  # 这一步也是
tele_num = tele_num.split("-")  # 用-将用户输入的分开

if tele_num[0] == "010":
    if "8" in tele_num[1]:

        if int(tele_num[1]) % 2 == 0:

            if int(tele_num[1]) % 3 == 0:
                cause.append("Yes")
            else:
                cause.append("不能被3整数")
        else:
            cause.append("不是偶数")
    else:
        cause.append("中没有8")
else:
    cause.append("不是来自北京")

if "Yes" in cause:
    print(tele_num_)
    print(f"{tele_num__} 是幸运号码")
else:
    print(tele_num_)
    print(f"{tele_num__} 不是幸运号码")
    print(f"{tele_num__} {cause[0]}")