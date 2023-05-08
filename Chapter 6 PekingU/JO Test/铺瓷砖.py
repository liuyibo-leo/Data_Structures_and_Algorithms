题目内容：
给定一个长度为N的区域，及4种不同长度的瓷砖：灰瓷砖（长为1格）、红瓷砖（长为2格）、绿瓷砖（长为3格）与蓝瓷砖（长为4格），求所有不同的铺满整个区域的方法数。
例如：当N=5时，共有15种铺满区域的方法，示意图如下：

输入格式:
一个自然数N

输出格式：
一行数字，表示不同的方法总数

输入样例：
5

输出样例：
15

def fillBlocks(blockList, blocks, knownResults):

    if blocks == 0: # 初步筛选的停止条件
        return 1
    elif knownResults[blocks] != 0: # 若清单中已有结果，则无需 recurrence
        return knownResults[blocks]
    else:
        numBlocks = 0 # 初始设置加总的数量值
        for i in [b for b in blockList if b <= blocks]:
            print('i', i)
            print('blockList', blocks)
            numBlocks = numBlocks + fillBlocks(blockList, blocks - i, knownResults) # 开始数据的最底层 recur, 并使用numBlocks进行加总
            knownResults[blocks]= numBlocks

    return numBlocks


blockLists = [1,2,3,4]
blocks = eval(input())
knownResults = [0] * (blocks + 1)

print(fillBlocks(blockLists,blocks,knownResults))
