#program to enter marks of 5 students into a list and display them in a sorted manner
#Marks of 5 students have to be entered
m1=float(input("Marks of 1st student:"))
m2=float(input("Marks of 2nd student:"))
m3=float(input("Marks of 3rd student:"))
m4=float(input("Marks of 4th student:"))
m5=float(input("Marks of 5th student:"))
#these marks have to be displayed in a sorted manner
SortedMarks=[m1,m2,m3,m4,m5] 
SortedMarks.sort() #built-in-function
print(SortedMarks)
