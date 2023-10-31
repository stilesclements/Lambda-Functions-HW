'''List comprehensions provide a concise way to create lists. 

It consists of brackets containing an expression followed by a for clause, then
zero or more for or if clauses. The expressions can be anything, meaning you can
put in all kinds of objects in lists.

The result will be a new list resulting from evaluating the expression in the
context of the for and if clauses which follow it. 

The list comprehension always returns a result list. '''


# Expression/transformation, iteration, condition/filter

'''
new_list = []
for i in original_list:
    if filter(i):
        new_list.append(expressions(i))  '''

#You can obtain the same thing using list comprehension:

# new_list = [expression(i) for i in original_list if filter(i)]


#The list comprehension starts with a '[' and ']', to help you remember that the
#result is going to be a list.

#There are 3 parts to list comprehension:

#*result*  = [*transform/expression*    *iteration*         *filter*     ]

#The filter part answers the question if the item should be transformed.






x=[i for i in range(10)]
print(x)

#add expression

squares=[x**2 for x in range(10)]
print(squares)

list1=[3,4,5]

multiplied=[item*3 for item in list1]
print(multiplied)


listOfWords=['this','is','a','list','of','words']

result=[word[0].upper() for word in listOfWords]
print(result)


#adding in an IF condition
# a new list of the square of all even number from 1 to 10
even_squares=[num**2 for num in range(1,11) if num%2==0]
print(even_squares)


string="Hello 12345 World"
numbers=[int(x) for x in string if x.isdigit()]
print(numbers)


list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list2=[]

list2=[x*100 for x in list1 if x%2==1]
print(list2)


infile=open('test.txt','r')
result=[x.rstrip('\n') for x in infile if 'line3' in x]
print(result)

def double(x):
    return x*2
print(double(10))


result=[double(x) for x in range(10) if x%2==0]
print(result)

result=[x+y for x in [10,30,50] for y in [20,40,60]]
print(result)

## Exercise ##

# 1 Using a list comprehension, create a new list called "newlist" out of the list "numbers", 
# which contains only the positive numbers from the list, as integers.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

newlist=[x for x in numbers if x>0]
print(newlist)

## 2 create a list of integers which specify the length of each word in
## a sentence except for the word 'the'

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()

word_len=[len(x) for x in words if x!='the']
print(word_len)

## Given dictionary is consisted of vehicles and their weights in kilograms. 
## Contruct a list of the names of vehicles with weight below 5000 kilograms. 
## In the same list comprehension make the key names all upper case.

dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, 
"Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

light_vehicle=[k.upper() for k,v in dict.items() if v<5000]
print(light_vehicle)


## Find all the numbers from 1 to 1000 that have a 4 in them

nums_with_4=[x for x in range(1,1001) if '4' in str(x)]
print(nums_with_4)

## count how many times the word 'the' appears in the text file - 'sometext.txt'

infile=open('sometext.txt','r')



count=0
# the_count=[word for line in infile for word in line.split() if word.lower()=='the']
# print(the_count)


for the in [word for line in infile for word in line.split() if word.lower()=='the']:
    count+=1
print(count)

## Extract the numbers from the following phrase ##

phrase = 'In 1984 there were 13 instances of a protest with over 1000 people attending. On average there were 15 reported injuries at each event, with about 3 or 4 that were classifled as serious per event.'


digits=[word for word in phrase.split() if word.isdigit()]
print(digits)



