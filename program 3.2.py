#Question 2
#calculator program
num1=float(input("Enter 1st no.:"))
num2=float(input("Enter 2nd no."))
#choice operation
print("Operation: +,-,*,/")
select=input("Select operations:")
#check operations and display result
#add two numbers
a=num1+num2
b=num1-num2
c=num1*num2
d=num1/num2
if select=="+":
    print(num1,"+",num2, "=",a)
elif select=="-":
    print(num1,"-",num2, "=",b)
elif select=="*":
    print(num1,"*",num2, "=",c)
elif select=="/":
    print(num1,"/",num2,"=",d)
else:
    print("invalid input")
        
                 
