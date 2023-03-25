# my answer
class Queue():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

def func(S):
    # your code here
    Q = Queue()
    lst = [S]
    min_s = min(lst)

    for q in S:
        Q.enqueue(q)
    for i in range(len(S)):
        Q.enqueue(Q.dequeue())
        # print(Q.items)
        output = ''.join(Q.items)
        if output < min_s:
            min_s = output
    return min_s

S = eval(input())
print(func(S))


# standard answer
def func(s):
    slength=len(s)
    minstring=s
    for j in range(slength):
        FirstChar=s[0]
        s=s[1:]
        s=s+FirstChar
        # print(s)
        if s<minstring:
            minstring=s
    return minstring

ss=eval(input())
print(func(ss))
