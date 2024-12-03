
#calculate
'''while True:
    n = int(input())
    if(n==1):
        a= int(input())
        b = int(input())
        print(a+b)
    if(n==2):
        a=int(input())
        b=int(input())
        print(a-b)
    if(n==3):
        a=int(input())
        b=int(input())
        print(a*b)
    if(n==4):
        a=int(input())
        b=int(input())
        print(a/b)
    if(n==5):
        a=int(input())
        b=int(input())
        print(a%b)
    if(n==6):
        sys.exit(0)
    if(n<1 and n>6):
        print("Invalid Operation")'''

#reverse a given number    
def reverse(n):
    rev=0
    while n>0:
        rem = n%10
        rev = (rev*10)+rem
        n = n//10
        return rev
n=int(input("Enter number to revers:"))
result = reverse(n)
print(result)