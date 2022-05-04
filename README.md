# python_week_1
first_number=None
second_number=None
while first_number is None:
    try:
        first_number= float(input("Enter first number: "))
    except:
        print('Please enter a number only')
while second_number is None:
    try:
        second_number= float(input("Enter second number: "))
    except:
        print('Please enter a number only')
        
summation=first_number+second_number
subtraction=first_number-second_number
multiplication=first_number*second_number
division= first_number/second_number
power=first_number**second_number
remainder=first_number%second_number

print("Sum is",summation, "\nSubtarction is",subtraction, "\nmultiplcation is",multiplication, "\ndivision is", division, "\npower is", power, "\nremainder is", remainder  )


