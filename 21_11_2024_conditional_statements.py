#if statements

str1 = "string1"
if str1=="string1" :
    print("Equal")

n=3
if n%2==0:
    print("n is even")
else:
    print("n is odd")
#if else if
num = 13
if num%2 == 0:
    print("num is devide by 2")
elif num%3 ==0:
    print("num is devided by 3")
else:
    print("number is odd")



    score = 75
    passing_score =70
    if score>= passing_score:
        print("You are pass")
    else :
        if score >= passing_score - 5 :
            print("You are almost passed")
        else :
            print("You are failed")


course="DataScience"
if course =="DataScience":
    print("You are in azads course")
elif course =="Physics":
    print("You are in Physics wallas course")
else:
    print("You are not enrolled")            

grade = 5
if grade>=7:
    print("Impressive skills")
elif grade>=5:
    print("You are doing well in physics wallas class")
else:
    print("Keep Working on your skills")

marks=75
if marks>=90:
    print("You got an 'A' Grade")