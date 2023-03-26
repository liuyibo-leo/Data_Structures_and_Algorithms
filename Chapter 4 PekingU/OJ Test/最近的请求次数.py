def func(mylist):
    output = []


    for k in mylist:
        times = 0
        for k_minus in mylist:
            if k_minus > k:
                break
            elif k_minus >= k - 10000:
                times = times + 1
        output.append(times)

    return output

mylist = eval(input())
print(func(mylist))

# 题目内容：
# 计算每个事件发生之时，往前算10000毫秒内有多少个事件发生，包含当事件；也即对于列表中的每个元素k，算出整个列表中有多少个元素介于k-10000和k（两端均含）之间。

# 输入格式:
# 一个已排序列表mylist，所有元素为非负整数，记录各个请求的发生时间，单位为毫秒。

# 输出格式：
# 一个与mylist等长的列表。

# 输入样例：
# [0,10,100,1000,10000,20000,100000]

# 输出样例：
# [1,2,3,4,5,2,1]
