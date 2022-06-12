#Question 2
y=int(input("Enter the year:"))
if (y%4==0 and y%100!=0) or (y%400==0 and year%100==0):
    print("The year",y,"is a leap year")
else:
    print("The year",y,"is not a leap year")
