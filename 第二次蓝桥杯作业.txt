# ===================================第一题===================================

def only_run(exp):  # 单个算式的计算栈
    num = exp.split("=")  # 进来的算式，用等号拆开
    ans, ques = num[0], num[1]  # 将算式的answer和question装进列表的1和2
    ans_run = eval(ans)  # 运行算式answer

    if str(ans_run) == ques:  # 如果运行结果和输入结果相同 （这个地方加不加str代表着会不会出现bug）
        list_output.append(f"{ans}={ques}")  # 正确，输出原答案
    else:
        list_output.append(f"{ans}={ques}(ANSWER:{ans_run})")  # 错误，输出正确答案
        numSon_list.append(1)  # 错误次数（不知道为什么，赋值不行，这个def里面检测不到，必须用列表来计数，导致我代码多了几行）

numSon_list, list_output = [], []  # 装错误次数的容器
num_more = input().split(" ")  # 输入端口；多个算式的计算1+1=2 4-3=1 5+5=10 12*12=141

for i in num_more:  # 因为题目要求给出多个算式，所以这样
    only_run(i)

print(f"{' '.join(map(str, list_output))} score:{int(100 - len(numSon_list) / len(num_more) * 100)}")  # 输出结果

# ===================================第一题 做法2===================================



error_count = 0  # 初始化错误计数


def only_run(exp):  # 单个算式的计算栈
    global error_count  # 申明全局变量
    num = exp.split("=")  # 进来的算式，用等号拆开
    ans, ques = num[0], num[1]  # 将算式的answer和question装进列表的1和2
    ans_run = eval(ans)  # 运行算式answer

    if str(ans_run) == ques:  # 如果运行结果和输入结果相同 （这个地方加不加str代表着会不会出现bug）
        list_output.append(f"{ans}={ques}")  # 正确，输出原答案
    else:
        list_output.append(f"{ans}={ques}(ANSWER:{ans_run})")  # 错误，输出正确答案
        error_count += 1  # 错误计数+1


list_output = []  # 装算式的容器
num_more = input("").split(" ")  # 输入端口；多个算式的计算1+1=2 4-3=1 5+5=10 12*12=141

for i in num_more:  # 因为题目要求给出多个算式，所以这样
    only_run(i)

print(f"{' '.join(map(str, list_output))} score:{int(100 - error_count / len(num_more) * 100)}")  # 输出结果



# ===================================第一题 做法3 去掉def并优化===================================

error_count = 0  # 初始化错误计数

num_more = input("").split(" ")  # 输入端口；并用空格分开为list；1+1=2 4-3=1 5+5=10 12*12=141

for i in num_more:  # 遍历列表的所有算式
    num = i.split("=")  # 进来的算式，用等号拆开

    if str(eval(num[0])) == num[1]:  # 如果运行结果和输入结果相同 （这个地方加不加str代表着会不会出现bug）
        print(f"{num[0]}={num[1]}", end=" ")  # 正确，输出原答案
    else:
        print(f"{num[0]}={num[1]}(ANSWER:{eval(num[0])})", end=" ")  # 错误，输出正确答案
        error_count += 1  # 错误计数+1
        
print(f"score:{int(100 - error_count / len(num_more) * 100)}")  # 输出结果



# ===================================第二题===================================

word, word_count = input(), input()  # 输入数据


def only_cont(word_, word_count_):  # 运算栈
    cont_number = 0  # 计数
    for i_ in word_:  # 打散一大段
        if i_ in word_count_:  # 如果有这个数，那就加一
            cont_number += 1
    return cont_number  # 返回一个计数


for i in word_count:
    count = only_cont(word, i)
    print(f"'{''.join(map(str, i))}'出现了{count}次")

# ===================================第二题/取消def解法===================================

word_more, word_key = input(), input()  # 初始化；输入数据
for i in word_key:  # 打散计数关键词，使之被单独的比对
    cont_number = 0
    for j in word_more:  # 打散大段字符，使之被单独喂入下一个循环
        if j in i:  # 如果有这个数，那就加一
            cont_number += 1
    print(f"'{''.join(map(str, i))}'出现了{cont_number}次")
