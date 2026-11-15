
# 2.3
grade = 91
if grade>=90:
print(f’Congratulations! Your grade of {grade} earns you an A in this\ course’)
# 2.4
left_operand = 27.5
right_operand = 2
sum = left_operand + right_operand
difference = left_operand - right_operand
product = left_operand * right_operand
quotient = left_operand / right_operand
floor_quotient = left_operand // right_operand
power = left_operand ** right_operand
print(f"The numbers are {left_operand} and {right_operand}\nTheir sum is {sum}\nTheir differnce is
{difference}\nTheir product is {product}\nTheir quotient is {quotient}\nTheir floor quotient is
{floor_quotient}\nTheir power is {power
# 2.5
radius = 2
pie = 3.14159
diameter = 2 * radius
circumference = 2*pie*radius
area = pie * radius**2
print (f"The diameter is {diameter}\nThe circumference is {circumference}\nAnd the area is {area}")
# 2.6
number = int(input("Enter any integer: "))
if number%2==0:
print("This integer is even")
else:
print("This number is odd")
# 2.7
if 1024%4==0:
print("4 is a multiple of 1024")
else:
print("4 is not a multiple of 1024")
if 10%2==0:
print("2 is a multiple of 10")
else:
print("2 is not a multiple of 10")
# 2.8
print ("Number\tSquare\tCube")number = 0
while 0<=number<=5:
number_square = number**2
number_cube = number**3
print (number,"\t",number_square,"\t",number_cube)
number = number+1
# 2.10
number1 = int(input(‘input first number: '))
number2 = int(input(input second number: '))
number3 = int(input(‘input third number: '))
sum = number1 + number2 + number3
average = sum/3
product = number1 * number2 * number3
smallest = number1
if number2<smallest
smallest = number2
if number3<smallest
smallest = number2
largest = number1
if number2>largest
largest = number2
if number3>largest
largest = number2
print (f"The sum is {sum}\nThe average is {average}\nThe product is {product}\nThe smallest is
{smallest}\nThe Largest is {largest}")
# 2.11
number = int(input(input a five digit number: '))
number1 = number//10000
number = number % 10000
number2 = number//1000
number = number % 1000
number3 = number//100
number = number % 100
number4 = number//10
number = number % 10
print (f"{number1} {number2} {number3} {number4} {number}")
# 2.14
user_age = int(input("Enter your age: "))
maximum_heartrate = 220 - user_age
target_heartrate1 = 50/100 * maximim_heartrate
target_heartrate2 = 85/100 * maximum_heartrate
print (f"Your maximum Heart-Rate is {maximum_heartrate}\nYour average Heart-Rate is within the range
of {target_heartrate1} and {target_heartrate2}")
# 2.12
principal = 1000
number_of_years1 = 10
number_of_years2 = 20
number_of_years3 = 30
amount1 = principal*(1 + 0.07)**number_of_years1
amount2 = principal*(1 + 0.07)**number_of_years2
amount3 = principal*(1 + 0.07)**number_of_years3
print (f"The Amount after 10 years is {amount1}\nThe Amount after 20 years is {amount2}\nThe Amount
after 30 years is {amount3}")
# 2.15
number1 = int(input(“input first number: “))
number2 = int(input(“input second number: “))
number3 = (input(“input third number: “))
if number1 <= number2 and number1 <= number3:
smallest = number1
if number2 <= number3:
middle = number2
largest = number3
else:
middle = number3
largest = number2
elif number2 <= number1 and number2 <= number3:
smallest = number2
if number1 <= number3:
middle = number1
largest = number3
else:
middle = number3
largest = number1
else:
smallest = number3
if number1 <= number2:
middle = number1
largest = number2
else:
middle = number2
largest = number1
print('Ascending order:', smallest,',', middle,',',largest''.)
 
