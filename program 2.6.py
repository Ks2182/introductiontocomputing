#Question6
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
ab_xor=a^b
count=0
while ab_xor:
    count=count+(ab_xor&1)
    ab_xor=ab_xor>>1
print(count)
