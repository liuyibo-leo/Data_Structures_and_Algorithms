# 题目内容：
# 给定一个表达式字符串，求出按不同的求值顺序可能得到的所有结果

# 输入格式:
# 一行字符串，仅包含0-9与运算符+、-与*
# 注：字符串保证三种运算符左右均为数字字符

# 输出格式：
# 所有不重复的可能的结果，从小到大排序并以半角逗号","分隔

# 输入样例：
# 2*3-4*5

# 输出样例：
# -34,-14,-10,10
# 注：
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10

# 示例代码模板：
# def findWays(expr):
#     # 用于将字符串转为数字与运算符，供参考
#     nums, ops = [], []
#     num = 0
#     for c in expr:
#         if '0' <= c <= '9':
#             num = num * 10 + ord(c) - 48
#         else:
#             ops.append(c)
#             nums.append(num)
#             num = 0
#     else:
#         nums.append(num)

#     # code here

# expr=input()
# print(findWays(expr))


# 解题思路
# 可以用递归算法解决，
# 将每一个运算符看作运算顺序中最后一个运算符，对其两侧表达式所有的可能的结果进行运算，把结果存入集合中，该集合即为整个表达式的所有可能结果。
# 基本结束条件：
# 1、当没有运算符时说明表达式只有一个数，表达式所有可能结果只有该数；
# 2、当只有一个运算符时，表达式所有可能结果只有一种，就是根据运算符对两个数进行对应运算的结果。
# 记得在函数返回时要先对结果进行去重，这样可以节省总体的运算时间

def findWays(expr):
    # 用于将字符串转为数字与运算符，供参考
    nums, ops = [], []
    num = 0
    for c in expr:
        if '0' <= c <= '9':
            num = num * 10 + ord(c) - 48
        else:
            ops.append(c)
            nums.append(num)
            num = 0
    else:
        nums.append(num)
# 以上为题目提供代码

    def calculation(nums, ops):
        if not ops:
            return [nums[0]]

        elif len(ops) == 1:
            if ops[0] == '+':
                return [nums[0] + nums[1]]
            elif ops[0] == '-':
                return [nums[0] - nums[1]]
            else:
                return [nums[0] * nums[1]]

        else:
            res = []
            for i in range(len(ops)):
                #将每一个运算符看作运算顺序中最后一个运算符，对其两侧表达式所有的可能的结果进行运算
                for num1 in calculation(nums[:i + 1], ops[:i]):
                    for num2 in calculation(nums[i + 1:], ops[i + 1:]):
                        #把结果存入集合中，该集合即为整个表达式的所有可能结果
                        res.append(calculation([num1, num2], [ops[i]])[0])

            return list(set(res)) #记得在函数返回时要先对结果进行去重，这样可以节省总体的运算时间

    return calculation(nums, ops)

expr = input()
a = findWays(expr)
a.sort()
print(','.join(str(i) for i in a))
