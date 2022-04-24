#program to store different data type values into a list
L1=[]  #empty List
SID=int(input("SID of the student:"))
L1.append(SID)  #Built-in-function
Name=str(input("Name of the student:"))
L1.append(Name)
Gender=str(input("Gender (F/M/U):"))
Gender=Gender.upper()  #Built-in-function
if Gender=='F' or Gender=='M' or Gender=='U': #condition
    L1.append(Gender)
else:
    print("Enter correct gender:")
    Gender=str(input("Gender (F/M/U)"))
    L1.append(Gender)
Course_name=str(input("Course name:"))
L1.append(Course_name)
CGPA=float(input("CGPA:"))
L1.append(CGPA) #Built-in-function
#Student[SID,Name,Gender,Course_name,CGPA]
print('Student',L1)
