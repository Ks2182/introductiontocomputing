#Question 1
#Reverse the string
def reverse(s):
    s=s[::-1]
    return s
s=input(" ")
print("The original string is:",end="")
print(s)
print("The reversed string is:",end="")
print(reverse(s))
