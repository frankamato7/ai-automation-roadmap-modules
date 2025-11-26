from calculator_app.calculator import add, subtract, multiply, divide

#Ask the user which operation they want
operation = int(input("""Which operation would you like?
      1) Addition
      2) Subtraction
      3) Multiplication
      4) Division
      """))

#Pick 2 numbers
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

#Perform the operation
if operation == 1:
    result = add(number_1,number_2)
elif operation == 2:
    result = subtract(number_1,number_2)
elif operation == 3:
    result = multiply(number_1,number_2)
elif operation == 4:
    result = divide(number_1,number_2)

print(f'Result: {result}')