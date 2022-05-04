# python_week_1
first_number = None
second_number = None
third_number = None
while first_number is None:
    try:
        first_number = float(input("Enter first number: "))
    except:
        print("Please enter a number only")
while second_number is None:
    try:
        second_number = float(input("Enter second number: "))
    except:
        print("Please enter a number only")
while third_number is None:
    try:
        third_number = float(input("Enter third number: "))
    except:
        print("Please enter a number only")

summation = first_number + second_number + third_number
subtraction = first_number - second_number - third_number
multiplication = first_number * second_number * third_number
division = (first_number / second_number) / third_number
power = (first_number**second_number) ** third_number
remainder = (first_number % second_number) % third_number

print(
    "Sum is",
    summation,
    "\nSubtarction is",
    subtraction,
    "\nmultiplcation is",
    multiplication,
    "\ndivision is",
    division,
    "\npower is",
    power,
    "\nremainder is",
    remainder,
)
