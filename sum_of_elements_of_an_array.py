list1 = []
i = 0
a = 0
#ask user to enter a numbers like 12 35 56 13
user_Input=input("enter numbers")  
#useing map function to short the code and remove the loop
list1= list(map(int, user_Input.split()))

print("array is:", list1)
#using inbuilt function of list to add the elemnts
a=sum(list1)
print("Sum of all the elements of the array is:",a)
