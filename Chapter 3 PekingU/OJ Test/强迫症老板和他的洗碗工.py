class stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def disWashing(data):
    s = stack()
    receipts = 0
    count = 0

    if s.isEmpty():
        s.push(count)

    while count < 10 and receipts < 10:
       if  s.isEmpty():
           count = count + 1
           s.push(count)

       elif s.peek() == data[receipts]:
           s.pop()
           receipts = receipts + 1
           # print('count', count)
           # print('re', receipts)
           # print(s.items)

       else:
           count = count + 1
           s.push(count)
           # print(s.items, 'two')

    if s.isEmpty():
        print('Yes')
    else:
        print('No')

 
disWashing(list(map(int, input())))


# 题目内容：洗碗工小明碰上了一位强迫症老板老王，餐厅一共就10只盘子，老板给仔细编上了0～9等10个号码，并要求小明按照从0到9的编号来洗盘子，当然，每洗好一只盘子，就必须得整齐叠放起来。
# 小明洗盘子期间，经常就有顾客来取盘子，当然每位顾客只能从盘子堆最上面取1只盘子离开。
# 老王在收银台仔细地记录了顾客依次取到盘子的编号，比如“1043257689”，这样他就能判断小明是不是遵照命令按照0123456789的次序来洗盘子了。
# 你也能像老王一样作出准确的判断吗？

# 输入格式:
# 长度为10的字符串，其中只包含0～9的数字，且不重复，代表顾客依次取到的盘子编号
# 输出格式：
# 字符串：Yes或者No，表示遵照次序洗盘子，或者没有遵照次序洗盘子

# 输入样例1：
# 1043257689
# 输出样例1：
# Yes

# 输入样例2：
# 4230178956
# 输出样例2：
# No
