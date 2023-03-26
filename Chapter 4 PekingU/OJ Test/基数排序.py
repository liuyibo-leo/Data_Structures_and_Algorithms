class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def radix_sort(s):
    # 请在此编写你的代码（可删除pass语句）
    #构建一个以10个队列为元素的列表
    qlist=[Queue() for i in range(10)]
    #构建一个main队列，存放未经排序的初始数
    mainQueue=Queue()
    #把列表中的存放未经排序的初始数加入队列中
    for token in s:
        mainQueue.enqueue(token)
    #得到列表中的最大数的位数
    numMaxChar=str(max(s))
    numMaxLen=len(numMaxChar)
    #得到所有数在第1~numMaxLen位的值，进行循环
    for i in range(numMaxLen):
        #把i的值转化为1~numMaxLen
        i=i+1
        #逐个把mainQueue中的值dequeue出来并进行相关操作
        for k in range(len(s)):
            #dequeue一个值
            token=mainQueue.dequeue()
            #得到这个值的位数
            tokenlen=len(str(token))
            #如果位数大于i，就可以得到真实的第i位的值
            if tokenlen>=i:
                places=int(str(token)[-i])
            #位数小于i，默认第i位为0
            else:
                places=0
            #把这个值放到对应的队列中
            qlist[places].enqueue(token)
        #把0~9队列中元素按顺序放回mainQueue
        for j in range(10):
            while not qlist[j].isEmpty():
                mainQueue.enqueue(qlist[j].dequeue())
    #把mainQueue中的值按顺序全部转到列表中
    result=[]
    while not mainQueue.isEmpty():
        result.append(mainQueue.dequeue())
    #返回列表
    return result
    # 代码结束
mylist = eval(input())
print(radix_sort(mylist))



# 题目内容：
# 实现一个基数排序算法，用于10进制的正整数从小到大的排序。
# 思路是保持10个队列(队列0、队列1......队列9、队列main)，开始，所有的数都在main队列，没有排序。
# 第一趟将所有的数根据其10进制个位(0~9)，放入相应的队列0~9，全放好后，按照FIFO的顺序，将每个队列的数合并排到main队列。
# 第二趟再从main队列队首取数，根据其十位的数值，放入相应队列0~9，全放好后，仍然按照FIFO的顺序，将每个队列的数合并排到main队列。
# 第三趟放百位，再合并；第四趟放千位，再合并。
# 直到最多的位数放完，合并完，这样main队列里就是排好序的数列了。

# 输入格式:
# 一个列表mylist，其中mylist包含一些需要排序的正整数，正整数互不相同且均不超过100000，且个数在1至1000之间。

# 输出格式：
# 一个与mylist等长的列表。

# 输入样例：
# [8, 91, 34, 22, 65, 30, 4, 55, 18]

# 输出样例：
# [4, 8, 18, 22, 30, 34, 55, 65, 91]
