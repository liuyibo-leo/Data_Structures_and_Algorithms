# 题目内容：
# 给定一个二叉查找树的节点插入顺序，请重新构建这个二叉查找树，并按从左至右顺序返回所有根节点至叶节点的路径

# 输入格式:
# 一行整数，以空格分隔
# 注：测试用例中不包含重复的数字；保证测试用例非空

# 输出格式：
# 按照叶节点由左至右顺序，以“根节点值->节点值->...->叶节点值”输出每条路径，每行输出一条
# 其中上述箭头号（->）的组成为一个半角减号（-）接上一个半角大于符号（>）

# 输入样例：
# 5 2 6 1 3 7 4

# 输出样例：
# 5->2->1
# 5->2->3->4
# 5->6->7

# 解题思路：
# 先构造二叉搜索树，接着前序遍历该二叉搜索树，到达叶节点时保存当前路径，最后分行打印所有路径


class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.val = None
        self.leftChild = left
        self.rightChild = right

    def put(self, key):
        if key < self.key:
            if self.leftChild:
                self.leftChild.put(key)
            else:
                self.leftChild = TreeNode(key)
        else:
            if self.rightChild:
                self.rightChild.put(key)
            else:
                self.rightChild = TreeNode(key)


def generateTree():
    root = TreeNode(lst[0])
    for i in lst[1:]:
        root.put(i)
    return root


def preorderTree(tree, path):
    path += str(tree.key)
    if not tree.leftChild and not tree.rightChild:
        result.append(path)
    else:
        path += '->'
        if tree.leftChild:
            preorderTree(tree.leftChild, path)
        if tree.rightChild:
            preorderTree(tree.rightChild, path)


lst = [int(num) for num in input().split()]
root = generateTree()
result = []
path = ''
preorderTree(root, path)
for p in result:
    print(p)
