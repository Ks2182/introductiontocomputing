#Question 4
import string, sys
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset=set(alphabet)
    return alphaset<=set(str1.lower())
a=input("Enter a sentence:")
print(ispangram(a))
