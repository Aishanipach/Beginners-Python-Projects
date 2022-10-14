n = int(input())
for i in range (0,n):
    print(" "*(n-i),"#"*i + str("#"*(i-1)))
for i in range(n,0,-1):
    print(" "*(n-i),"#"*i + str("#"*(i-1)))
