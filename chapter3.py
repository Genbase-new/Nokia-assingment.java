# 3.12
number = int(input("input number: "))
constant_number = number
reverse = 0
while number>0:
    reverse = reverse*10 + number%10
    number = number//10
if reverse == constant_number:
    print ("This is a palindrome")
else:
    print ("This is not a palindrome")


# 3.7
print ("Number\tSquare\tCube")
number = 0
while 0<=number<=5:
    number_square = number**2
    number_cube = number**3
    print (f'{number:>5}\t{number_square:>5}\t{number_cube:>5}')
    number = number+1


# 3.8
sum = 0
product = 1
score = int(input ("Enter Score: "))
smallest = score
largest = score
sum += score
product *= score
for number in range (1,4):
    score = int(input ("Enter Score: "))
    sum += score
    product *= score
    if score<smallest:
        smallest = score
    if score>largest:
        largest = score
average=sum/4
print ("Sum: ",sum)
print ("Product: ", product)
print ("Average: ", average)
print ("Smallest: ", smallest)
print ("Largest: ",largest)


# 3.9
for year in range(1, 31):
    amount = 1000 * ((1 + 0.05) ** year)
    print(f'{year:>2}{amount:>10.2f}')


# 3.11
number = int (input("Enter digit: "))
Product = 1
for counter in range (number,0,-1)
    Product = product * number
print('the factorial of ',number ,'is ', factorial)


# 3.20
binary_number= int (input("Enter Binary Number: "))
stable_number = binary_number
counter = 0
sum=0
while binary_number>0:
    singular_number = binary_number%10
    binary_changer = singular_number * (2**counter)
    sum+=binary_changer
    binary_number=binary_number//10
    counter+=1
print(f"The decimal of the binary number {constant_number} is {sum}")


# 3.21
cents = int (input("Enter amount in cents: "))
quarters = 30
quarter_counter = 0
dimes = 5
dimes_counter = 0
pennies = 1
pennies_counter = 0
if cents>quarters:
    quarter_counter= cents//quarters
    cents = cents%quarters
if cents>dimes:
    dimes_counter = cents//dimes
    cents = cents % dimes
if cents > pennies:
    pennies_counter = cents//pennies
print (f"Change is: \n{quarter_counter} Quarters\n{dimes_counter} Dimes\n{pennies_counter} Pennies")


# 3.11
gallons_counter = 0
gallons = 0
sum_of_gallons = 0
sum_of_miles = 0
while gallons = -1:
    gallons = int (input("Enter the gallons used (-1 to end): "))
    if gallons == -1:
        break
    miles = int (input("Enter the miles driven: "))
    miles_per_gallon = miles/gallons
    sum_of_gallons += gallons
    sum_of_miles += miles
    print ("The miles/gallon is ",miles_per_gallon)
total_miles_per_gallon = sum_of_miles/sum_of_gallons
print ("The overall average miles/gallon is ",total_miles_per_gallon)
