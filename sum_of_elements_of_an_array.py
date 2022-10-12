list1 = []
i = 0
a = 0
print("Input numbers and enter 'end' to stop inputing")
while i < 1:
    x = input()
    if x == "end":
        break
    elif x.isdigit():
        list1.append(int(x))
    else:
        print("INVALID INPUT")
print("array is:", list1)

for i in range(0, len(list1)):
    a += list1[i]    

print("Sum of all the elements of the array is:",a)
