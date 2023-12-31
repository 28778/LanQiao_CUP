# 10行 ===================================第一题 做法3 去掉 def 并优化，去掉了不必要的赋值===================================

error_count = 0  # 初始化计数（错误了多少题）

num_more = input("").split(" ")  # 输入端口；并用空格分开为 "[]"

for i in num_more:  # 遍历列表的所有算式
    num = i.split("=")  # 进来的算式，用等号拆开（请记住这个num，它代表着用列表 "[]" 装的单个算式的 "=" 的左右部分，分别被存在了 num[0] 和 num[1] ）

    if str(eval(num[0])) == num[1]:  # 是否错误（加 str 代表着 "1+1=02" 这样的算式是错误的）
        print(f"{num[0]}={num[1]}", end=" ")  # 正确，输出原答案
    else:
        print(f"{num[0]}={num[1]}(ANSWER:{eval(num[0])})", end=" ")  # 错误，输出正确答案（这个eval直接被我装进输出端，措不及防的）
        error_count += 1  # 错误计数+1

print(f"score:{int(100 - error_count / len(num_more) * 100)}")  # 输出分数

# 7行 ===================================第二题 取消 def 并优化，去掉了不必要的赋值===================================

word_more, word_key = input(), input()  # 输入数据

for i in word_key:  # 遍历关键词
    cont_number = 0

    for j in word_more:  # 遍历需要比对的字段

        if j in i:  # 如果 i 里面有 j 有这个数，那就加一次
            cont_number += 1

    print(f"'{''.join(map(str, i))}'出现了{cont_number}次")

# 3行 ===================================第二题 取消 def 并优化，去掉了不必要的赋值，使用count函数===================================

word_more, word_key = input(), input()  # 输入数据
for i in word_key:  # 遍历关键词
    print(f"'{i}'出现了{word_more.count(i)}次")
