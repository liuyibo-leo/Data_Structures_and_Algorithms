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
