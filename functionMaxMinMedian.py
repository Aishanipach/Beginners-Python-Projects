def bth(a, b, c, d, e):
    return max(a, b, c, d, e)

def sml(a, b, c, d, e):
    return min(a, b, c, d, e)

def aritmetic_median(a, b, c, d, e):
    return (a+b+c+d+e)/5

def main():
    n1 = int(input(" "))
    n2 = int(input(" "))
    n3 = int(input(" "))
    n4 = int(input(" "))
    n5 = int(input(" "))

    mx = bth(n1, n2, n3, n4, n5)
    mnr = sml(n1, n2, n3, n4, n5)
    median = aritmetic_median(n1, n2, n3, n4, n5)

    print(f'biggest number {mx}, smallest number {mnr}, aritimetic median: {median}.')

if __name__== '__main__':
    main()