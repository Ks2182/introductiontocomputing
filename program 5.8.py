#Question 8
a=int(input("Enter a value:"))
b=int(input("Enter a value:"))
c=int(input("Enter a value:"))
d=int(input("Enter a value:"))
e=int(input("Enter a value:"))
f=int(input("Enter a value:"))
g=int(input("Enter a value:"))
h=int(input("Enter a value:"))
i=int(input("Enter a value:"))
j=int(input("Enter a value:"))
list1=[a,b,c,d,e,f,g,h,i,j]
#positive or negative numbers
for i in list1:
    if i>0:
     print("Positive number:",i)
    elif i<0:
        print("Negative number:",i)
#even or odd numbers
for j in list1:
    if j%2==0:
        print("Even number:",j)
    else:
        print("Odd number:",j)
#number of times each number occurs in the list
def counter(list1,x):
    count=0
    for item in list1:
        if (item==x):
            count=count+1
    return count
x=int(input("Enter the value whose count you want to find in the list:"))
y=counter(list1,x)
print("The element",x, "appears",y, "times in the list")
