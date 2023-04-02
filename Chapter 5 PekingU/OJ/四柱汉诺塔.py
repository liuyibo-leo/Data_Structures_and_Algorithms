def move(height, a, b, c, d):
    # print(step)
    if step[height] != None:
        return step[height]

    else:
        min = 100000 # why min = 100000
        for k in range(1, height):
            count = 0
            count = count + move(height - k, a, b, d, c)
            # print('1st count', count)
            count = count + pow(2, k) - 1
            # print('2nd count', count)
            count = count + move(height - k, c, a, b, d)
            # print('3rd count', count)
            if count < min:
                min = count

        step[height] = min
        return min

height = int(input())
step = [0, 1, 3, 5]
stepLen = len(step)
step.extend([None] * (height - (stepLen - 1))) # why minus 3? 因为半包含，且在函数中需要与height在step中的定位对比，故需要在steplen中减1
print(move(height, 'a', 'b', 'c', 'd'))

# 题目内容：
# 如课上所说，汉诺塔问题源于印度一个古老传说。对于原始的汉诺塔游戏，可供玩家操作的空间一共只有三根柱子，导致按原传说的要求，需要超过1.8*10^19步才能解开。
# 透过新增柱子可以大幅度地减少需要的步数。此处要求在给出指定的盘数，柱子数量为4（即限制为4根柱子）且不改变原有传说的其他规则的限制下，找出完成迁移的最小步骤数。

# 输入格式:
# 一个非负整数M，M代表盘数，M<=1000。

# 输出格式：
# 一个非负整数，表示完成迁移的最小步骤数。

# 输入样例：
# 3

# 输出样例：
# 5
