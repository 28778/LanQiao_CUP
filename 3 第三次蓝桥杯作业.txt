# 计算电梯耗电量
power = 0


def x(list1):  # 判断楼的上下，并将耗电量相加
    global power
    if list1[0] < list1[1]:  # 那就是在上升，所以+1
        if list1[0] < 0 and list1[1] > 0:  # 取消掉0层
            power += (list1[1] - list1[0])
            power -= 1
        else:
            power += (list1[1] - list1[0])

    else:  # 下降，所以+0.3
        if list1[0] > 0 and list1[1] < 0:  # 取消掉0层
            power += (list1[0] - list1[1]) * 0.3
            power -= 0.3
        else:
            power += (list1[0] - list1[1]) * 0.3


# 输入数据
user_input = input().split(",")

for i in range(0, len(user_input) - 1):
    i1 = i + 1
    user_input[i], user_input[i1] = int(user_input[i]), int(user_input[i1])  # 并将str转换为int
    list_only = [user_input[i], user_input[i1]]  # 将 1,2,3,4 分割成 1,2 2,3 3,4 方便进入耗电量比对
    x(list_only)
print(round(power, 2))



# 计算数字相加
input_1, input_2, num_1 = int(input()), int(input()), 0  # 初始化各个值
input_2 += 1  # 加一，因为后面会用到range

input_1 = str(input_1)
for i in range(1, input_2):
    num = input_1 * i
    num_1 += int(num)
print(num_1)