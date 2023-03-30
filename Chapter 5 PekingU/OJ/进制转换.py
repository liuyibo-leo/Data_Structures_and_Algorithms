class stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

tStack = stack()
nStack = stack()

# def toTen(input_num, m):
#     converString = '0123456789'
#     if input_num < m:
#         tStack.push(converString[input_num])
#         print('<', tStack.items)
#     else:
#         tStack.push(converString[input_num % m])
#         print(tStack.items)
#         toTen(input_num//m, m)
#
#     resultOne = ''.join(map(str, tStack.items))
#     print('resultOne', resultOne)
#     return resultOne

def toTen(input_num, m):
    resultOne = int(input_num, m)
    # print(resultOne)
    return resultOne

def toN(result, n):
    result = int(result)
    converString = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if result < n:
        nStack.push(converString[result])
        # print('2<', nStack.items)
    else:
        nStack.push(converString[result%n])
        # print(nStack.items)
        toN(result//n, n)
    finalResult = ''.join(map(str, nStack.items))
    return finalResult


m, n = map(int, input().split(' '))

# num = int(input())
num = input()
result = toTen(num, m)

print(toN(result, n))


# 题目内容：
# 给定一个M进制的数，请将其转换为N进制并输出

# 输入格式:
# 两行，第一行为空格分隔的两个数字，分别为10进制表示的M与N；其中M, N均满足2 ≤ M、N ≤ 36
# 第二行为待转换的M进制数字，其中每位超过9的部分从10至36分别用大写字母A-Z表示；输入数据保证数据的每一位不超过M

# 输出格式：
# 一行字符串，表示转换后的N进制数

# 输入样例：
# 8 16
# ‭471‬

# 输出样例：
# ‭139
