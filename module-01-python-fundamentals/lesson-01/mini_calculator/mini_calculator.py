
name = input("What is your name? ")
print(f"Nice to meet you, {name}!")
number1 = input(f"Give me a number, {name}: ")
first_number = int(number1)
number2 = input(f"Give me another number, {name}: ")
second_number = int(number2)

addition_operation = first_number + second_number
subtraction_operation = first_number - second_number
multiplication_operation = first_number * second_number
division_operation = first_number / second_number

print(f"""
Hi, {name}! Here are your results:
{first_number} + {second_number} = {addition_operation}
{first_number} - {second_number} = {subtraction_operation}
{first_number} * {second_number} = {multiplication_operation}
{first_number} / {second_number} = {division_operation}
""")