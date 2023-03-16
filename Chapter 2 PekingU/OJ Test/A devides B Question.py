a = int(input())
b = int(input())

if b != 0:
    result = a/b
    print('%.3f'%result)
else:
    print('NA')
    
    #输出一个数，即他们的商，保持小数点后3位（%.3f）
    #如果除数为0，则输出：NA（两个字母）
    #1/2 = 0.500
    #2/0 = NA
