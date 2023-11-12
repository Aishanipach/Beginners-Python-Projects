#Given a positive integer N, print the sum of cubes of 1st N natural numbers.

n = int(input())
sum = 0
for i in range(0,n+1):
    k = i*i*i
    sum = sum +k
print(sum)
