#Question 6
a=int(input("Enter triangle side 1:"))
b=int(input("Enter triangle side 2:"))
c=int(input("Enter triangle side 3:"))
e=a+b>c and a+c>b and c+b>a
match e:
    case True:
        print("Yes")
    case False:
        print("No")
