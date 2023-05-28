# 题目内容：
# 在一个小镇里，按从 1 到 N 标记了 N 个人。传言称，这些人中有一个是小镇上的秘密法官。

# 如果小镇的法官真的存在，那么：
# 小镇的法官不相信任何人。
# 每个人（除了小镇法官外）都信任小镇的法官。
# 只有一个人同时满足属性 1 和属性 2 。

# 给定列表 trust，该列表由信任对 trust[i] = [a, b] 组成，表示标记为 a 的人信任标记为 b 的人。
# 如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的标记。否则，返回 -1。

# 输入格式:
# 输入包含两行，第一行为一个正整数N，第二行为信任对列表trust，以合法的Python表达式给出

# 输出格式：
# 一个整数，表示法官的编号

# 输入样例：
# 4
# [[1,3],[1,4],[2,3],[2,4],[4,3]]

# 输出样例：
# 3

# 参考代码模板：
# def findJudge(N,trust):
#     # code here
#     pass

# N = int(input())
# trust = eval(input())
# print(findJudge(N, trust))


def findJudge(N, trust):
    count = [0] * (N + 1)
    for i, j in trust:
        count[i] -= 1
        count[j] += 1
    for i in range(1, N + 1):
        if count[i] == N - 1:
            return i
    return -1
 
 
N = int(input())
trust = eval(input())
print(findJudge(N, trust))
