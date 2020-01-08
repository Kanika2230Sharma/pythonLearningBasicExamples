# birthYear = input('What year were you born?')
# age = 2019 - int(birthYear)
# print(f'your age is {age}')

# userName = input('Enter username')
# passWord  = input('Enter password')
# codedPass = '*' * len(passWord)
# print(f'Hi {userName}, your password {codedPass} is {len(passWord)} letters long' )

# is_magician = True
# is_expert = False
# if not is_magician:
#   print('You need magic powers')

# elif is_magician and is_expert:
#   print('You are a master magician')

# elif is_magician and not is_expert:
#   print('Atleast you know magic')

#COUNTER
# myList = [1,2,3,4,5,6,7,8,9,20,10]
# counter = 0
# for item in myList:
#   counter += 1
# print(f'No of elements in list is {counter}')


# for i,num in enumerate(list(range(100))):
#   if num == 50:
#     print(f'index of 50 is {i}')

#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]
# for i,item in enumerate(picture):
#   for newItem in item:
#     if newItem:
#       print('*', end = '')
#     else:
#       print(' ',end = '')
#   print()
  
#DUPLICATE EXERCISE
# someList = ['a','b','c','d','b','n','m','n','n']
# newList = sorted(someList)
# duplicateList = []
# i = 0
# occurrence = 0
# while i < len(newList):
#   occurrence = newList.count(newList[i])
#   if occurrence > 1:
#     for item in duplicateList:
#       if item != newList[i]:
#         duplicateList.append(newList[i])
# print(duplicateList)

#calculate age function

# def checkDriverAge(age = 0):
#   if age < 18:
#     print("Sorry, you are too young to drive this car. Powering off")
#   elif age > 18:
#     print("Powering On. Enjoy the ride!");
#   elif age == 18:
#     print("Congratulations on your first year of driving. Enjoy the ride!")

# #age = input("What is your age?: ")
# checkDriverAge(18)

#Rule to pass parameters :
#params,*args,default, **kwargs

#Exercise-highest even in a list

# high = 0
# def highestEven (list):
#   
#   for item in list:
#     global high #another way of using this is to give global high in parameters and argument of call 
#     if item % 2 == 0 and item > high:
#       high = item
#   return high

# print(highestEven([1,3,22,4,20,11,13,10,33,34]))
#can have use even list and then find max of list using max()

 #Scope - what variables do I have access to?
# def outer():
#     x = "local"
#     def inner():
#         nonlocal x #causing this x as parent variable x
#         x = "nonlocal"
#         print("inner:", x)
#     inner()
#     print("outer:", x)
# outer()

#1 - start with local
#2 - Parent local?
#3 - global
#4 - built in python functions


# #Given the below class:
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # 1 Instantiate the Cat object with 3 cats
# catChi = Cat('Chi',2)
# catChou = Cat('Chou',5)
# catChichi = Cat('Chichi',3)

# # 2 Create a function that finds the oldest cat
# def getOldest(chiAge,chouAge,chichiAge):
#   if chiAge >chouAge and chiAge >chichiAge:
#     return chiAge
#   elif chouAge > chiAge and chouAge > chichiAge:
#     return chouAge
#   else:
#     return chichiAge

# # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
# print(f"The oldest cat is {getOldest(catChi.age,catChou.age,catChichi.age)} years old")


# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# def oldest_Cat(a,b,c):
#     if( a.age > b.age )and (a.age > c.age):
#         return a
#     elif b.age > c.age:
#         return b
#     else:
#         return c
    
# cat_1 = Cat("zoozoo",3)
# cat_2 = Cat("zoodoo",2)
# cat_3 = Cat("zooby",4)

# old = oldest_Cat(cat_1,cat_2,cat_3)

# print("The oldest cat is {} years old.".format(old.age))

# 
##Zip function in Functional Programming
# my_List = [1,2,3]
# your_tuple = (10,20)

# print(list(zip(my_List,your_tuple)))

# #QUESTIONS on map,filter,reduce and zip
# from functools import reduce
# #1 Capitalize all of the pet names and print the list
# my_pets = ['sisi', 'bibi', 'titi', 'carla']

# def capitalize(string):
#     return string.upper()

# print(list(map(capitalize, my_pets)))


# #2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5,4,3,2,1]

# print(list(zip(my_strings, sorted(my_numbers))))


# #3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88]

# def is_smart_student(score):
#     return score > 50

# print(list(filter(is_smart_student, scores)))


# #4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
# def accumulator(acc, item):
#     return acc + item

# #print(reduce(accumulator, (my_numbers + scores)))
# print(reduce(accumulator,scores,reduce(accumulator,my_numbers)))
# #LAMBDA EXPRESSION
# # lambda param: action(param)
# #square of input list
# my_List = [2,3,4,5]
# print(list(map(lambda item : item * item, my_List)))

# #take an input list of tuple and sort the list on the basis of second number of tuple
# my_List = [(2,3),(10,-1),(2,0),(1,5)]
# my_List.sort(key = lambda i:i[1])
# print(my_List)

#LIST,set,DICTIONARY COMprehension exercise
# some_List = ['a','b','c','c','d','e','e','e']
# duplicate_List = {item for item in some_List if some_List.count(item) > 1} 
# print(list(duplicate_List))

#DECORATORS
#performance decorator.
# from time import time
# def performance(fn):
#   def wrapper(*args, **kwargs):
#     t1 = time()
#     result = fn(*args, **kwargs)
#     t2 = time()
#     print(f'took {t2-t1}')
#     return result
#   return wrapper

# @performance
# def long_time():
#     for i in range(10000):
#         i*5

# long_time()

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
# user1 = {
#     'name': 'Sorna',
#     'valid': True #changing this will either run or not run the message_friends function.
# }

# def authenticated(fn):
#   def wrapper(x): #better way to use *args and **kwargs
#     if x['valid'] == True:
#       return fn(x)
#   return wrapper

# @authenticated
# def message_friends(user):
#     print('message has been sent')

# message_friends(user1)

##GENERATORS
#FIBONACCI series
 #new learning to print first instead of third
# def febonacci_gen(num):
#   first = 0
#   second = 1
  
#   for i in range(num):
#     yield first 
#     temp = first   #can be done like first,second = second, first + second
#     first = second
#     second = temp + second

# for i in febonacci_gen(5):
#   print(i)

#Exercise Questions Day 1
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

# for item in range(2000,3201):
#   if item % 7 == 0 and item % 5 != 0:
#     print(item, end = ',')
# print("\b")   # this will cause the cursor to break from existing line and come to new line

#Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320

# def factorial(num):
#   fact = 1
#   while(num):
#     fact = fact * num
#     num = num-1
#   return fact

# number = int(input('factorial of which number need to be calculate '))
# print(factorial(number), end = ',')

# #Using While Loop
# n = int(raw_input())
#  #input() function takes input as string type
#                      #int() converts it to integer type
# fact = 1
# i = 1
# while i <= n:
#     fact = fact * i;
#     i = i + 1
# print(fact)
# #Using For Loop
# n = int(input()) 
# #input() function takes input as string type
# #int() converts it to integer type
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)
# #Using Lambda Function

# n = int(input())
# def shortFact(x): return 1 if x <= 1 else x*shortFact(x-1)
# print(shortFact(n))

# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8

# Then, the output should be:

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

#Exercise To check whether two input strings are anagram or not

def anagramCheck(string1,string2):
  if string1.sort() == string2.sort():
    return True
   
string1 = input('Enter two strings to check for anagram: String1: ')
string2 = input('String2: ')
print(anagramCheck(string1,string2))


