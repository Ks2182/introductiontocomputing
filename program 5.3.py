#Question 3
#area of a triangle
a=float(input("Enter first side:"))
b=float(input("Enter second side:"))
c=float(input("Enter third side:"))
if a+b>c and b+c>a and c+a>b:
    #semi perimeter
    s=(a+b+c)/2
    #area
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print("The area of the triangle is:",area)
else:
    print("error")
