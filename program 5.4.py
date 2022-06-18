#Question 4
#pattern using nested for loop
k=4
for i in range(11):
    if i<4:
        for j in range(i+1):
            print("*",end="")
        print("\n")
    elif i>4:
        for j in range(k+1):
            print("*",end="")
        print("\n")
        k=k-1
