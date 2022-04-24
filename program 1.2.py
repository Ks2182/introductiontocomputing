#program to compute a person's income tax
#tax rate= 20% =0.20
tax_rate=0.20
#standard income in $
sta_ded=10000
#dependent income in $
dep_ded=3000
gross_income=int(input("Enter gross income:"))
numb_of_dep=int(input("Enter number of dependent:"))
#Taxable income= gross income - standard deduction - (dependent deduction* no. of dependents)
Tax_income=gross_income-sta_ded-(dep_ded*numb_of_dep)
print("Total taxable income:",Tax_income)
#Tax= Taxable income * tax rate
Tax=Tax_income*tax_rate
print("Tax (in $) is:",Tax)

