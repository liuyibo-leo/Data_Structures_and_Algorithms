# 谢尔宾斯基地毯
# 展示地毯
def weave(n,whole):
    for line in whole:
        print(''.join(line))
    return
# 雕刻地毯
def carpet(N, array, startR, startC):
    if N == 3:
        array[startR + 1][startC + 1]=' '*len(c)
        return
    else:
        # 镂空中心位置
        for row in range(N // 3, 2 * N // 3):
            for col in range(N // 3, 2 * N // 3):
                array[row + startR][col + startC] = ' '*len(c)
        # 镂空环绕位置
        for row in range(3):
            for col in range(3):
                if [row, col] != [1,1]: # 跳过中心位置
                    carpet(N // 3, array, startR + row * N // 3, startC + col * N // 3)

n=int(input())
c=input()
# 新建地毯
whole = [[c]*n for i in range(n)]
# 雕刻地毯
carpet(n,whole,0,0)
# 展示地毯
weave(n, whole)



# 谢尔宾斯基地毯是形如上图的正方形分形图案，每个地毯可分为等大小的9份，其中中央挖空，其余均由更小的地毯组成。
# 现给定地毯大小（行数）与组成地毯的字符元素，请打印相应的地毯图形。
# 注：空腔以半角空格表示；当给定字符元素长度不为1时空格数须与字符长度对应

# 输入格式:
# 输入为两行，分别为地毯大小正整数N与组成元素字符串c
# 输入数据保证N为3的正整数幂

# 输出格式：
# 由N行长度为N*len(c)的字符串构成的谢尔宾斯基地毯

# 输入样例：
# 9
# []
