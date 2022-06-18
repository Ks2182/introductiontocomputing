#Question 5
rows=int(input("Enter :"))
print("Pattern is:")
alphabet=65
for i in range(rows):
    for j in range(i+1):
        print('%c'%alphabet,end="")
        alphabet=alphabet+1
    print()
