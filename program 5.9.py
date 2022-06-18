#Question 9
#program to count the number of occurrences of each word in the list
def counter(list1,x):
    count=0
    for item in list1:
        if (item==x):
            count=count+1
    return count
#creating an empty list
list1=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    item=input()
    #add item in the list
    list1.append(item)
x=input("Enter the word whose count you want to find in the list:")
y=counter(list1,x)
print("The element",x, "appears",y, "times in the list")



