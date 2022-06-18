#Question 7
#numbers which are multiple of 7 and divisible by 11
lower=1
upper=500
for i in range (lower,upper+1):
    if(i%7==0 and i%11==0):
        print(i)
