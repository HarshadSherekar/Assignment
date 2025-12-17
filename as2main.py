import as2module as calc
n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
operator=input("enter operators(+,-,*,/)")

if operator=='+':
    result=calc.add(n1,n2)

elif operator=='-':
    result=calc.subtract(n1,n2)

elif operator=='*':
    result=calc.multiply(n1,n2)

elif operator=='/':
    result=calc.divide(n1,n2)
print("final result=",result)    