list1 = []
i = 0
a = 0

#ask user to create list
print("Input numbers and input @ to stop inputing")
while i < 1:
    x = input()
    if x == "end":
        break
    else:
        list1.append(x)

#swap elements of list
print(list1)
print("select two positions to be swapped")
n = int(input("first position: "))
m = int(input("Second position: "))

if n <= len(list1) and m <= len(list1):
    list1[n-1],list1[m-1] = list1[m-1], list1[n-1]
    print(list1)
else:
    print("INVALID POSITIONS")
