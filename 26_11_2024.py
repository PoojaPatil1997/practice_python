#for loop 

string1 ="123456789"
for ch in range(-1,-10,-1):
    print(ch)
    print("\t",string1[ch])

#home work
#1.write a program to print numbers from 1 to 20 using a for loop

for i in range(1,21):
    print(i)

#2.write a program to print sum of first n natural numbers
num=0
for i in range(1,11):
    num = num+i
    if i==10:
        print(num)

 #3.write a program to display the multiplication table of 5 using table
for i in range(1,11):
    print(i,"*5\t",i*5)

#4.write a program to iterate over a list of fruits and print each fruit's name

fruits = ['Apple','bananna','mango','stoberry','pynapal','orange']
for f in range(len(fruits)):
    print(fruits[f])

 #5.write a program to print even numbers  between order using a for loop

for n in range(1,21):
    if n%2==0:
        print(n)

#6.write a program to print numbers from 10 to 1 using a for loop

for i in range(10,0,-1):
    print(i)

#7.write a program to print square of numbers from 1 to 10 using a for loop

for i in range(11):
    print("square of",i,"is",i*i)


#8.write a program to calculate factorial of a number using loop
'''num1 = input("Enter a  number to calculate factorial")
num = int(num1)
for i in range(1,num):
    num =i*num
    print(num)'''

#9.write a program to find the sum of all elements in a list
lst = [2,3,4,5,6,7,8,9]
sum = 0
for i in range(len(lst)):
    sum = sum+lst[i]
    if i==len(lst)-1:
        print(sum)

#10.write a program to check given number is prime number or not
num2 = input("Enter number to check is it prime or not")
num_to_check = int(num2)
cnt =0
for i in range(2,num_to_check):
    if num_to_check%i ==0:
        cnt = cnt+1
    if i == num_to_check-1:
        if cnt==0:
            print(num_to_check,"is a prime number")
        else:
            print(num_to_check,"is a not prime number")
            
