# 题目内容：
# 有 n 门课程要选，其编号分别由 0 至 n-1
# 每个课程都有一些需要提前学完的先修课程：例如，假设在学习课程 0 前需要先学习课程 1 ，我们用一个先修关系对[0, 1]来表示这种 “后学习课程，先修课程” 的关系
# 现给定一系列课程与若干先修关系，请判断是否存在一个方案可以学完所有课程

# 输入格式:
# 输入分为两行，第一行为一个整数，表示课程的总数
# 第二行为一个嵌套列表的Python表达式，包含若干先修关系对

# 输出格式：
# True或False，表示是否存在一个按照先修关系学完所有课程的顺序

# 输入样例：
# 2
# [[1,0],[0,1]]

# 输出样例：
# False

# 参考代码模板：
# def canFinish(self, n, pre):
#     # code here
#     pass

# n = int(input())
# pre = eval(input())
# print(canFinish(n, pre))

# 解题思路：
# 判断是否存在一个按照先修关系学完所有课程的顺序就是判断课程依赖关系图中是否不存在圈，先用一个列表存储每个课程是哪些课程先修课程，用一个递归算法来判断从图中任意顶点出发是否存在圈，递归运算过程中记录已经访问过的课程和当前路径中的课程，如果当前路径中的课程出现重复说明出现了圈，如果遇到已经访问过但不在当前路径中的课程可以直接跳过从而加速递归运算。

def canFinish(n, pre):
    if n == 0:
        return False
    graph = [[] for _ in range(n)]
    for sub in pre:
        graph[sub[1]].append(sub[0])

    def isCircle(N):
        visited.append(N)
        if N in path:
            return True
        path.append(N)
        keys = graph[N]
        if keys == []:
            return False
        for key in keys:
            if key in visited and key not in path:
                continue
            if isCircle(key):
                return True
            path.pop()
        else:
            return False

    i = 0
    while i < n:
        visited = []
        path = []
        if isCircle(i):
            return False
        i += 1
    else:
        return True


n = int(input())
pre = eval(input())
print(canFinish(n, pre))
