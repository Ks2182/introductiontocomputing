#Question 5
#enter a hyphen- separated sequence of words
n=input("enter the string: ") 
l=n.split('-') 
l.sort() 
print('-'.join(l))
