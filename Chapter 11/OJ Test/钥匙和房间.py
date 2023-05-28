# 题目内容：
# 有 N 个房间，开始时你位于 0 号房间。每个房间有不同的号码：0，1，2，...，N-1，并且房间里可能有一些钥匙能使你进入下一个房间。

# 在形式上，对于每个房间 i 都有一个钥匙列表 rooms[i]，每个钥匙 rooms[i][j] 由 [0,1，...，N-1] 中的一个整数表示，其中 N = rooms.length。 钥匙 rooms[i][j] = v 可以打开编号为 v 的房间。

# 最初，除 0 号房间外的其余所有房间都被锁住。
# 你可以自由地在房间之间来回走动。
# 请判断是否可以最终打开所有房间。

# 输入格式:
# 一行嵌套列表，列表长度为N，以合法的Python表达式格式给出

# 输出格式：
# True或False，代表是否可以进入每个房间

# 输入样例：
# [[1],[2],[3],[]]

# 输出样例：
# True

# 参考代码模板：
# def canVisitAll(rooms):
#     # code here
#     pass

# rooms = eval(input())
# print(canVisitAll(rooms))


# option 1

#深度优先
def canVisitAll(rooms):
    room_map = {0} 
    def enterroom(keys):
        for key in keys:
            if key not in room_map:
                room_map.add(key)
                enterroom(rooms[key])
            else:
                pass
        return
    enterroom(rooms[0])
    return len(room_map)==len(rooms)
 
 
rooms = eval(input())
print(canVisitAll(rooms))

# option 2

# 广度优先
def canVisitAll(rooms):
    visited, queue = {0}, [0]
    while queue:
        room_index = queue.pop()
        for key in rooms[room_index]:
            if key not in visited:
                visited.add(key)
                queue.insert(0,key)
    return len(visited) == len(rooms)
 
rooms = eval(input())
print(canVisitAll(rooms))

