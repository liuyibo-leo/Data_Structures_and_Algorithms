# 题目内容：
# 给定以嵌套列表形式给出的多叉树，求它的后序遍历
# 注：每个代表非空多叉树的列表包含至少一项；列表第一项代表节点值，其后每一项分别为子树；遍历子树时以列表下标从小到大的顺序进行。

# 输入格式:
# 一行合法的Python表达式，可解析为嵌套列表形式的多叉树结构

# 输出格式：
# 一行整数，以空格分隔

# 输入样例：
# [1,[2,[3,[4],[5]],[6]],[7],[8,[9],[10]]]

# 输出样例：
# 4 5 3 6 2 7 9 10 8 1

def postorderTree(tree):
    if len(tree) == 1:
        return tree
    else:
        result = []
        for i in range(1, len(tree)):
            result += postorderTree(tree[i])
        result += [tree[0]]
        return result


lst = eval(input())
postorder = postorderTree(lst)
print(*postorder)

