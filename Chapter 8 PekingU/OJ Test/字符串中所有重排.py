题目内容：
给定一个字符串s与待查找字符串p，请给出使得s[i:i+len(p)]是p的一个字母重排的所有下标i
题目保证字符串p非空，且各字符串仅由小写字母构成

输入格式:
两行字符串，第一行为s，第二行为p

输出格式：
所有满足条件的下标从小到大排列，以空格分隔输出
若无对应下标，则输出字符串"none"

输入样例：
abababa
ab

输出样例：
0 1 2 3 4 5

输入样例2：
a
b

输出样例2：
none


def findAnagrams(s, p):
    s_len = len(s)
    p_len = len(p)
    l = []
    p_list = [0 for _ in range(26)]
    s_list = [0 for _ in range(26)]
    for i in p:
        p_list[ord(i) - ord('a')] = p_list[ord(i) - ord('a')] + 1
    i = 0
    while i <= s_len - p_len:
        for x in s[i:i + p_len]:
            s_list[ord(x) - ord('a')] = s_list[ord(x) - ord('a')] + 1
        if s_list == p_list:
            l.append(i)
        s_list = [0 for _ in range(26)]
        i = i + 1
    if len(l) == 0:
        return ['none']
    else:
        return l
 
s = input()
p = input()
print(*findAnagrams(s, p))
