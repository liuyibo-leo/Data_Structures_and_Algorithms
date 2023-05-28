# 题目内容：
# 你现在手里有一份大小为 M x N 的『地图』（网格） grid，上面的每个『区域』（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地
# 对于每个海洋方格，其存在一个距离它最近的陆地方格，相应有一个到陆地的最小距离
# 请输出上述所有最小距离中的最大值。

# 我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 - x1| + |y0 - y1| 。

# 如果地图上只有陆地或者海洋，请返回 -1。

# 输入格式:
# 输入共1行，为一个仅包含0与1的嵌套列表，用合法的Python表达式给出

# 输出格式：
# 一个整数，表示最短距离

# 输入样例：
# [[1,0,1],[0,0,0],[1,0,1]]

# 输出样例：
# 2
# 注：最远的海洋区域坐标为(1,1)

# 参考代码模板：
# def maxDistance(grid):
#     # code here
#     pass

# grid=eval(input())
# print(maxDistance(grid))

def maxDistance(grid):
    # 地图规模
    n, m = len(grid), len(grid[0])
    # 每个点到陆地的曼哈顿距离
    dist = [[float('inf') for _ in range(m)] for _ in range(n)]
    # 该点是否被访问过
    visited = [[False for _ in range(m)] for _ in range(n)]
    # 队列
    q = []
    # 陆地计数
    cnt = 0
    ans = 0
    tot = n * m
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                dist[i][j] = 0
                visited[i][j] = True
                q.append((i, j))
                cnt += 1
    # 如果都是陆地或者都是海洋，则返回-1
    if cnt == tot or cnt == 0:
        return -1
    while q:
        x, y = q.pop(0) # 出列
        for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            # 如果坐标合法并且没被访问过
            if 0 <= i < n and 0 <= j < m and not visited[i][j]:
                dist[i][j] = min(dist[i][j], dist[x][y] + 1) # 取最小值
                ans = max(ans, dist[i][j]) # 更新答案
                visited[i][j] = True
                q.append((i, j)) # 入列
    return ans
 
 
grid = eval(input())
print(maxDistance(grid))
