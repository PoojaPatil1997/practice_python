#Conditional Statements
### Simple Conditional Questions


'''1. Check a number 
    Write a program to check if a number is positive, negative, or zero.'''

num = -10
if num > 0 :
    print("Number is Possitive")
elif num < 0 :
    print("Number is Negative")
else:
    print("Number is 0")



'''2. Check even or odd  
   Write a program to check if a given number is even or odd.'''

num = 20
if num>0:
    print("Even")
else :
    print("Odd")



'''3. Grade Checker  
   Write a program to display grades based on a percentage:
   - A: 90-100
   - B: 70-89
   - C: 50-69
   - F: Below 50'''

marks = 49

if marks>=90 and marks<=100 :
    print("A: 90-100")
elif marks>=70 and marks<=89:
    print("B: 70-89")
elif marks>=50 and marks<=69:
    print("C: 50-69")
else:
    print("F: Below 50'''")




''' 4. Check divisibility  
   Check if a given number is divisible by 3, 5, or both.'''

num = 132
if num>0 :
    if num%3==0 and num%5==0 :
        print("Number is divisible by 3,5 both")
    elif num%3==0 :
        print("Number is divisible by 3")
    elif num%5==0 :
        print("Number is divisible by 5")
    else:
        print("Number is no divisible by 3 or 5")
else:
    print("Invalid Number...")



'''5. Minimum of two numbers  
   Find the smaller number between two given numbers.'''

num1 = 350 
num2=100
if num1<num2 :
    print("First Number is smaller")
elif num1>num2 :
    print("Second Number is smaller")
else:
    print("Both Numbers are equal")



'''### Nested Conditional Questions
6. Find the largest of three numbers  
   Given three numbers, find the largest using nested if statements.'''

num1=50
num2=60
num3=40
if num1>num2 :
    if num1>num3:
        print("Number1 is greater")
    else:
        print("Number 3 is greater")
else:
    if num2>num3 :
        print("Number 2 is greater")
    else:
        print("Number 3 is greater")




'''7. Check leap year  
   Write a program to check if a given year is a leap year or not:
   - Divisible by 4 and not 100, or divisible by 400.'''

year = 300
if year%400==0 :
    print("Year is a leap year")
elif year%100 ==0 :
    print("Year is not a leap year")
elif year%4 == 0 :
    print("Year is a leap year")
else:
    print("Year is not a leap year")



'''8. Nested temperature check  
   Categorize temperature into:
   - Cold: Below 15°C
   - Warm: 15°C to 30°C
   - Hot: Above 30°C'''

temperature = 40
if temperature<30:
    if temperature>=15 and temperature<=30:
        print("Warm")
    else:
        print("cold")
else:
    print("Hot")



'''9. Vowel or consonant  
   Check if a given character is a vowel or consonant.'''

character = 'A'
if character=='a' or character=='e'or character=='i'or character=='o'or character=='u'or character=='A'or character=='E'or character=='I'or character=='O'or character=='U':
    print("character is a vowel")
else:
    print("character is a  consonant")



'''10. Driving eligibility  
    Check if a person is eligible to drive:
    - Must be 18 or older.
    - Nested check for possessing a valid license.'''

age_of_person = 17
if age_of_person>0 :
    if age_of_person>=18 and age_of_person<=60 :
        print("eligible to drive")
    else:
        print("Not eligible to drive")
else:
    print("Invalid Age...")

'''### Advanced Logical Questions
11. Triangle validation  
    Check if three sides can form a triangle:
    - The sum of any two sides must be greater than the third side.'''

side1 = 1
side2 = 10
side3 = 12
if side1+side2>side3:
    if side2+side3>side1:
        if side3+side1>side2:
            print("form a valid triangle")
        else:
            print("not form a valid triangle")
    else:
        print("not form a valid triangle")
else:
    print("not form a valid triangle")




'''12. Calculate tax based on salary  
    Determine the tax rate:
    - Salary ≤ 5,00,000: 5%
    - 5,00,001 - 10,00,000: 10%
    - Above 10,00,000: 20%'''

salary = 600000
if salary>0:
    if salary>=500000:
        print("tax=",5/100*salary)
    elif salary>=500001 and  salary<=1000000 :
        print("tax=",10/100*salary)
    else:
        print("tax=",20/100*salary)
else:
    print("Invalid Salary....")

    
'''13. Categorize age  
    Categorize a person's age:
    - 0-12: Child
    - 13-19: Teen
    - 20-59: Adult
    - 60+: Senior'''

age=75
if age<0:
    print("Invalid age..")
else:
    if age<=12:
        print("Child")
    elif age>=13 and age<=19:
        print("Teen")
    elif  age>=20 and age<=59:
        print("Adult")
    else:
        print("Senior")


'''14. Logical AND check  
    Check if a number is greater than 10 and divisible by 2.'''

number=59
if number>10 and number%2==0:
    print("number is greater than 10 and divisible by 2")
else:
    print("number is not greater than 10 or divisible by 2")




'''15. Logical OR check  
    Check if a number is less than 5 or greater than 20.'''

number=59
if number<5 or number>20:
    if  number<5:
        print("Number is less than 5")
    else:
         print("Number is greater than 20")
else:
    print("number is not less than 5 nor greater greater than  20")



'''### Application-Based Scenarios
16. Electricity bill  
    Calculate an electricity bill:
    - Usage ≤ 100 units: ₹5/unit
    - 101-200 units: ₹10/unit
    - Above 200 units: ₹15/unit'''

eusage = 201
if eusage<=100:
    print("Charges 5rs/unit...\nelectricity bill:=",5*eusage)
elif eusage>=101 and eusage<=200:
    print("Charges 10rs/unit...\nelectricity bill:=",10*eusage)
else:
    print("Charges 15rs/unit...\nelectricity bill:=",15*eusage)



'''17. Season finder  
    Find the season based on the month:
    - December-February: Winter
    - March-May: Spring
    - June-August: Summer
    - September-November: Autumn'''

month="act"
winter = ("december","Jan","feb")
Spring = ("mar","april","may")
Summer = ("June","july","august")
Autumn = ("sep","act","nov")
if month in winter:
    print("Winter")
elif month in Spring:
    print("Spring")
elif month in Summer:
    print("Summer")
else:
    print("Autumn")



'''18. Password validation  
    Check if a password meets these conditions:
    - At least 8 characters. - 
    Contains the character '@''' 

password="abcd1234@"
lenthofpass = len(password)
if lenthofpass>=8 :
    if "@" in password:
        print("Valid Password")
    else:
        print("Password should contain @")
else:
    print("Password length should be greater than 8 character")
    

'''19. Categorize BMI  
    Categorize Body Mass Index (BMI):
    - Below 18.5: Underweight
    - 18.5 - 24.9: Normal
    - 25 - 29.9: Overweight
    - 30 or higher: Obese'''
    
bmi = 10.20
if bmi >0:
    if bmi<18.5:
        print("Underweight")
    elif bmi>=18.5 and bmi<24.9:
        print("Normal")
    elif bmi>=25 and bmi<29.9:
        print("Overweight")
    else:
        print("Obese")
else:
    print("Invalid BMI")



'''20. Character type checker  
    Check if a given character is:
    - Alphabet
    - Digit
    - Special character'''

char = '.'
if char.isdigit():
    print("given Character is digit")
elif char.isalpha():
    print("given Character is alphabet")
else:
    print("given Character is Special character")