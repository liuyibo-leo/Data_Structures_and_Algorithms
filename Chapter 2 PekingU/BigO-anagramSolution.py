def anagramSolution(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        print(('pos', pos)) #pos is just a position to locate the position in the 26 alphabets
        print('old:', c1)
        c1[pos] = c1[pos] + 1
        print('new', c1)

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOk = True

    while j < 26 and stillOk:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillOk = False

    return stillOk

print(anagramSolution('apple', 'pleap'))
