x = int(input())
y = int(input())
list1 = []
if x>y:
    x,y = y,x

for i in range (x,y+1):
    for j in range(2,i//2):
        if i%j == 0:
            break
    else:
        list1.append(i)
print(list1)
