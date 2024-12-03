'''
-Python is case sensetive compiler & interprited highlevel language.
-Interprited language mean's it reads code line by line.
-Python works like union in c.In python we don't need to declare datatypes because it uses shared memory space. so last updated value we will get in paython

_____________DATA TYPES IN PYTHON_______________
Int,Float,String,Bulian,Complex,Set,List,Tupal,Dictionary
'''
#INT DATA TYPE
age = 20   #No need to explicitly declare data type, Direct assigned value 
print(age) #print is a function whic is used to display message on screen
print(type(age)) # type is also one kind of function or reserved-keyword that shows data type of age

#FLOAT DATA TYPE
price = 68.20 
print(price)
print(type(price)) 

#STRING DATA TYPE
# STRING IN PYTHON IS INMUTABLE BUILD IN DATA TYPE
#***1****
name = "pooja" #Valid String Quotes).
name1 = 'pooja' #Valid String Quotes).
name2 = " It's pooja" #Valid String Quotes).
print(name,name1,name2)
print(type(name))

#***2****



#SET DATA TYPES
set = {1,'a',3,4.3,5} #It is same as array but we can make array of variables  having any data types.
print(set)
print(type(set)) 

#DICTIONARY DATA TYPE
dic = {1:'a',2:'b',3:'c',4:'d'} #when you want key:value pair use dictionary data type
print(dic)
print(type(dic)) 

Grand_Father_family = {'Son_1':{'doughter':'neha','son':'pruthvi'},'Son_2':{'doughter':'asha','son':'raj'}} #we can even create dictionary under dictionry

#TUPLE DATA TYPE
#Tuples buildin data type in python it is immutable means values we can not change like string
# difference list [],tuple()
# methods in tuples index,count
 
newtuple = (5,6,7,8,1,2,2,2,3,4,5,)
print(newtuple)
print(type(newtuple)) 
print(newtuple.count(2))
print(newtuple.index(2))

#LIST DATA TYPE
# build in data type,multiple type of data we can store in one list,list is mutable in python(direct change happen on main location)
marks = [60,90,98,95,99,97]
print(marks)
print(type(marks))
student = ["pooja",27,"sangli"]
print(student)
print(type(student))
#list Slicing
#list_name[starting_inx:ending_inx]
print(marks[1:3]) #starting index will print end endex-1 will print

#methods of list in python
#append,sort,sort(reverse=True),reverse(),insert,remove element,pop perticuler index value delete,count count perticular element occurance

marks.append(4) #appends value at the end of list
marks.append(10)
marks.sort() #sorts the list in assending order
print(marks)
marks.sort(reverse=True) #sorts the list in desending order
print(marks)
marks.insert(1,9) #inserts 9 at index 1
print(marks)
marks.remove(9) #removes 9 from the list
print(marks)
marks.pop(0) #pop o th index value from list
print(marks) 
print(marks.count(4)) #counts occurance of 4 in the list
print(marks) 
marks.reverse() #reverse list
print(marks) 
