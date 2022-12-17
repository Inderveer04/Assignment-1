gross_income= int(input('Enter your gross income '))
std_deduction= 10000
dependent= int(input('Enter your dependents '))
dep_deduction= 3000
formula= gross_income-std_deduction-(dependent*dep_deduction)
tax= formula*0.2
print(tax)