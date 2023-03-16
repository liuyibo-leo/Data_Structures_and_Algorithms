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

def crossOff(data):
    s = stack()
    for i in data:
        if s.isEmpty():
            s.push(i)
        elif s.peek() == i:
             s.pop()
        else:
            s.push(i)
    return s.items

result = crossOff(input())
print(''.join(result)) #join the items together with or the mark of '' in a list, like: ['b', 'p', 'x', 'y', 'z']


#题目内容：开心消消乐我们都熟悉，我们可以用刚学过的栈来做一个“一维”的开心消消乐游戏，这个游戏输入一串字符，逐个消去相邻的相同字符对。如果字符全部被消完，则输出不带引号的“None”
#输入格式:一个字符串，可能带有相邻的相同字符，如“aabbbc”
#输出格式:一个字符串，消去了相邻的成对字符，如“bc”
