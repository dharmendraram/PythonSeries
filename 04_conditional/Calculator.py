print('''
    + Add
    - Sub
    * Multiply
    / Divide
''')
num1 = float(input("Enter The number 1:"))
num2 = float(input("Enter The number 2:"))
opr =input("Enter The Operator(+,-,*,/):-")

# if opr=='+':
#     print(num1+num2)
# elif opr=='-':
#     print(num1-num2)
# elif opr=='*':
#     print(num1*num2)
# elif opr=='/':
#     print(num1/num2)
# else:
#     print("Invalid Operation..")


if opr=='+':
    print(num1+num2)
if opr=='-':
    print(num1-num2)
if opr=='*':
    print(num1*num2)
if opr=='/':
    print(num1/num2)
if opr!="+" and opr!="-" and opr!="*" and opr!="/":
    print("Invalid Operation..")
