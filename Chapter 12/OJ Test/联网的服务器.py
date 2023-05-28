# 题目内容：
# 给定一个二维列表表示的地图，其中每个位置值为 1 或 0 ；1 代表该位置存在一个服务器，0 代表该位置为空。对每个服务器来说，如果其所在的位置同一行或同一列有其它服务器，就称这个服务器是“联网”的。
# 请求出地图上所有联网的服务器的总数。

# 输入格式:
# 一行，为一个以合法Python表达式给出的二维嵌套列表

# 输出格式：
# 一行整数

# 输入样例：
# [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]

# 输出样例：
# 4

# 解题思路：
# 用两个列表分别存储每一行和每一列各有多少台服务器，当发现当前位置存在服务器时，就到列表中查看该服务器的行和列上是否存在其他服务器。

def netSum():
    x_list = [0] * len(list)
    y_list = [0] * len(list[0])
    count = 0
    for i in range(len(list)):
        for j in range(len(list[0])):
            if list[i][j] == 1:
                x_list[i] += 1
                y_list[j] += 1
    for i in range(len(list)):
        for j in range(len(list[0])):
            if list[i][j] == 1:
                if x_list[i] >= 2 or y_list[j] >= 2:
                    count += 1

    return count


list = eval(input())
print(netSum())
