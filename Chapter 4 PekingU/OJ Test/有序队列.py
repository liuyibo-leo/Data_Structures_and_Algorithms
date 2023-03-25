# my answer
class Queue():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

def func(S):
    # your code here
    Q = Queue()
    lst = [S]
    min_s = min(lst)

    for q in S:
        Q.enqueue(q)
    for i in range(len(S)):
        Q.enqueue(Q.dequeue())
        # print(Q.items)
        output = ''.join(Q.items)
        if output < min_s:
            min_s = output
    return min_s

S = eval(input())
print(func(S))


# standard answer
def func(s):
    slength=len(s)
    minstring=s
    for j in range(slength):
        FirstChar=s[0]
        s=s[1:]
        s=s+FirstChar
        # print(s)
        if s<minstring:
            minstring=s
    return minstring

ss=eval(input())
print(func(ss))


# 题目内容：
# 一开始给出了一个由小写字母组成的字符串 S。我们规定每次移动中，选择最左侧的字母，将其从原位置移除，并加到字符串的末尾。这样的移动可以执行任意多次
# 返回我们移动之后可以拥有的最小字符串（注：在Python3中，字符串的大小可用不等号比较）。

# 输入格式:
# S。S为仅含有小写字母的字符串，长度不超过100000。

# 输出格式：
# 一个与S等长的字符串。

# 输入样例：
# "cba"

# 输出样例：
# acb
