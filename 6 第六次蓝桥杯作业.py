# 解法1（数学方法）
def josephus(n, k):
    if n == 1:
        return 1
    else:
        return 1 + (josephus(n - 1, k) + 2) % n
people = int(input())
print(josephus(people, 3))

#解释一下 1 + (josephus(n - 1, k) + 2) % n这个公式

# k的意思是报数的数，n的意思是人

# + 1 是因为在计算的过程中，我们从1开始计数而不是从0开始，所以要将结果加1。

# josephus(n - 1, k) 递归调用，表示问题规模减小到n - 1个人时的解。也可以说，我们假设我们已经知道了n - 1个人时的解。

# + 2 计算下一个要退出的人的位置。
# 因为我也不知道怎么解释，在数学上的“报数”就是要-1，不然就会报4个。
# 而且这个数要随着“题目要求的报数”来改变

# % n 这是取模运算，确保计算的位置在当前问题规模下的有效范围内。如果超过了n，就会循环回到起点。


# 解法2（简单的解法）

# 这个解法的关键在于把圈想象成一排队列，没报到3的人自动去队列的最后。

people_num = 5
people_li = list(range(1, people_num + 1))  # 创建一个队伍
watchdog = 0  # 初始化计数器

while len(people_li) > 1:
    bdr = people_li.pop(0)  # 弹出第一个人，装到
    watchdog += 1

    if watchdog == 3:
        watchdog = 0  # 重置计数器（因为没有被添加到末尾，这个人就out了）
    else:
        people_li.append(bdr)  # 将这个人追加到列队的末尾

print(people_li[0])



# 递枕头
people = int(input())  # 人数
time_require = int(input())  # 规定时间

people_num = 1  # 初始化“编号记录器”

while time_require > 0:  # 如果还有时间
    if people_num < people:  # 如果没到头，就正常地递枕头
        people_num += 1  # “编号记录器”+1
        time_require -= 1  # 时间-1
    else:  # 如果到头了，那么就用减法反着递枕头，直到到第一个人
        while time_require > 0:
            people_num -= 1
            time_require -= 1
            if people_num == 1:  # 如果到了第一个人，那就跳出，运行正向递枕头
                break

print(people_num)
# 如果计数为0，那么输出
