#ask user to enter a numbers like 12 35 56 13
user_Input=input("enter numbers")  
#useing map function to short the code and remove the loop
list1= list(map(int, user_Input.split()))
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
