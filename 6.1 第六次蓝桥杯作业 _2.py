# 用最拙劣的技术敲出最不可靠的代码

dd = 1000  # 设定迭代次数
li = []  # 初始化列表
input_ = int(input())

while dd > 0:  # 我想迭代1000次，每次迭代减少一条鱼
    fish_all = 0
    fish_n = 0
    fish_output = 0

    people = input_
    time = people
    
    dd -= 1  # 迭代-1
    fish = dd  # 将鱼的数量设为迭代的数

    while time > 0:
        fish_n = (fish - 1) / people  # 将鱼丢掉1只，且分成n份

        if fish_n % 1 == 0 and fish_n != 0:
            fish = fish - fish_n - 1  # 计算剩下多少鱼
            fish_output += 1 + fish_n
            if time == 1:
                fish_output += fish
            time -= 1
        else:
            fish_all, fish_n, fish_output = 0, 0, 0  # 重置数据
            break

    if fish_n == 0:  # 这个if语句用于判断数据是否有效，无效则丢弃重来。
        continue
    else:
        li.append(people), li.append(fish_output), li.append(fish_n)  # 将每个可行解装入列表
print(f"{li[-3]}个人共捕了至少{int(li[-2])}条鱼\n最后一个人拿走了{int(li[-1])}条鱼")  # 最优解其实就是列表中的最后三个数




# 小明新年第一天得到了一个苹果，他就去帮妈妈把碗洗了。妈妈很高兴。于是，之后每天早上妈妈都会给他一个苹果。小明舍不得吃苹果，都放在冰箱里，
# 每逢双数天的下午，爸爸都会来偷吃小明的苹果，偷吃的数量，是当天天数的最后一位的数字。如果是第4天，偷吃4个，第6天，偷吃6个，第10天，那就偷吃0个（没偷吃）。
#
# 妈妈第一时间就发现了，马上把苹果补上：
# ①如果爸爸把苹果吃光了(最多吃冰箱中的数量)，那就补给他当天被吃掉苹果的双倍。
# ②如果没有吃光，就补上剩下苹果的 ½（如果除不开，就只保留整数部分，至少一个苹果），
# ③当天下午刚被偷吃就补（例如：第二天下午，两个苹果都被吃光了，马上补当天吃掉的两倍，就是补4个苹果，这样第二天晚上就有4个苹果）。
# ④但是如果不偷吃，就不补。
#
# 来帮小明算算，到n(n < 366)天的晚上，还有多少苹果？
# 输入描述:第一天中午的苹果数和想查看第n天晚上的苹果数，空格分开。
# 输出描述:第n天晚上的苹果数
input_ = input().split(" ")

# 初始化
apple = int(input_[0]) - 1  # 等于起始的苹果
day_over = int(input_[1])  # 等于结束的天数

day = 1

# 先算出n天剩下的苹果
while day_over > 0:
    # print("======第", day, "天（apple+1）======")
    # 奖励苹果
    apple += 1
    # print("有", apple, "个苹果")
    # 判断是否要偷吃
    if day % 2 == 0 and day % 10 != 0:
        eat = day % 10  # 偷吃当天个位数的天数个
        apple_bei = apple
        apple -= eat
        # print("偷吃了", eat)
        if apple < 0:
            eat = apple_bei
            apple = 0
            # print("偷吃了", eat)
        # print("偷吃之后还剩", apple, "个苹果")
        # 若吃了，就补回
        # ①如果爸爸把苹果吃光了(最多吃冰箱中的数量)，那就补给他当天被吃掉苹果的双倍。
        if apple == 0:
            apple += apple_bei * 2
            # print("补回了", apple_bei * 2)
        # ②如果没有吃光，就补上剩下苹果的 ½
        elif apple >= 0:
            if int(apple * 0.5) == 0:  # 如果除不开，就只保留整数部分，至少一个苹果
                apple += 1
                # print("补回了", "1")
            else:
                apple += int(apple * 0.5)
                # print("补回了", int(apple * 0.5))
        # print("今天晚上剩了", apple)
    day += 1
    day_over -= 1

print(apple)
