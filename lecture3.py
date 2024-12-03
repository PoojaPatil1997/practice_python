# list
# build in data type,multiple type of data we can store in one list,list is mutable in python(direct change happen on main location)

# marks = list[90,80,65,56,78,98]

# student_list = list["student1", 95.80,"delhi"]
# print(student_list)

#list Slicing


#list_name[starting_inx:ending_inx]

# marks1 = [90, 80, 65, 56, 78, 98]

# print(marks1[1:5])

#methods of list in python
#append,sort,sort(reverse=True),reverse(),insert,remove element,pop perticuler index value delete,count count perticular element occurance

# list = [1,2,3]
# list.append(4)
# list.append(10)
# list.append(7)
# list.append(5)
# list.sort()
# list.sort(reverse= True)
# list.insert(1,9)
# list.remove(9)
# list.pop(0)
# print(list.count(2))
# print(list)


#Tuples buildin data type in python it is immutable means values we can not change like string
# difference list [],tuple()
# methods in tuples index,count

# newtuple = (5,6,7,8,9,2,3,4,4,4,)
# print(newtuple.count(4))
# print(newtuple.index(4))

# list_movies = []
# movie1 = input("Enetr Name of first movie:")

# movie2 = input("Enetr Name of second movie:")

# movie3 = input("Enetr Name of third movie:")

# list_movies.append(movie1)
# list_movies.append(movie2)
# list_movies.append(movie3)
# print(list_movies)

#if list contain palindrom then print palindrom element

list1 = ["maam","pooja","rar","this"]
listcopy = list1.copy()
listcopy.reverse()
print(listcopy)
