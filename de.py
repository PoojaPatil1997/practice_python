
n = int (input("Enter number\n"))
i=1
m=1
while i<=n:
    j=1
    bg =''
    while j<=n:
        if j==i or j==1:
            bg+=str(i)
        else:
            bg+=str('0')
        j+=1
        print(bg)
    i+=1
    