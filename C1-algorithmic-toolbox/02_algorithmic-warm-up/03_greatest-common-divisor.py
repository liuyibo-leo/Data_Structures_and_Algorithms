def GCD(a, b):

    if a>b:
        a1 = b
        b1 = a

    if b1 == 0:
        print('gcd is ', a1)
        gcd = a1
    else:
        gcd = b1%a1

    re_gcd = []
    while gcd != 0:
        re_gcd.append(gcd)
        b1 = a1
        a1 = gcd
        gcd = b1 % a1
        if gcd == 0:
            return(re_gcd[-1])

a, b = input().split(' ')
a = int(a)
b = int(b)

print(GCD(a, b))


##################################
# A Smarter Way!!!

n = input()
a, b = map(int, n.split())

def gcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)

print(gcd(a, b))
