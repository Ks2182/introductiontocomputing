#Question 1
ma_rks=int(input("Enter marks:"))
if ma_rks<25:
    print("Grade:F")
elif ma_rks>=25 and ma_rks<=45:
    print("Grade:E")
elif ma_rks>=45 and ma_rks<=50:
    print("Grade:D")
elif ma_rks>=50 and ma_rks<=60:
    print("Grade:C")
elif ma_rks>=60 and ma_rks<=80:
    print("Grade:B")
else:
    print("Grade:A")
    
