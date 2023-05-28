# 题目内容：
# 给定一个指定大小N的散列表，并输入一系列数字：若找到空槽，则插入该数字，并返回槽位置；若该数字在散列表中存在，则直接输出其位置。
# 注：使用下标增加的二次探测法解决散列冲突
# 注2：散列表实际大小应确定为不小于用户输入N的最小质数

# 输入格式:
# 两行
# 第一行为用户指定散列表大小N
# 第二行为一系列数字，以空格分隔

# 输出格式：
# 逐个输出对应数字在散列表中位置，以空格分隔
# 若该数字无法插入，则输出“-”

# 输入样例：
# 4
# 10 6 4 10 15

# 输出样例：
# 0 1 4 0 -

# 参考代码模板：
# def createHashTable(n):
#     # code here
#     pass

# def insertNumbers(table, nums):
#     # code here
#     pass

# n = int(input())
# nums = list(map(int, input().split()))
# table = createHashTable(n)
# insertNumbers(table, nums)

def createHashTable(n):
    for i in range(2, n):
        if n % i == 0:
            n = n + 1
    else:
        return n
 
 
def insertNumbers(table, nums):
    lst = []
    for i in range(len(nums)):
        j = nums[i] % table
        if j not in lst:
            lst.append(j)
        else:
            found = 0
            a = i
            while(not found):
                for x in range(a):
                    if nums[x] == nums[a]:
                        found = 1
                        break
                break
            if found == 1:
                lst.append(lst[x])
            else:
                for m in range(1,table):
                    k = (nums[i] + m*m) % table
                    if k not in lst:
                        lst.append(k)
                        break
                else:
                    lst.append("-")
    return lst
n = int(input())
nums = list(map(int, input().split()))
table = createHashTable(n)
print(*insertNumbers(table, nums))
