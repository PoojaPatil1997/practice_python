'''def sum_even_odd_digites(number):
    rem=0
    odd=0
    even=0
    while number>0:
        rem = number%10
        if rem%2==0:
            even=even+rem
        else:
            odd=odd+rem
        number = number//10 
    if number==0:
        print("Sum of even & odd digites is:",even,"&",odd)
        
num = int (input("Enter number to calculate sum of odd&even digites:"))
sum_even_odd_digites(num)'''

