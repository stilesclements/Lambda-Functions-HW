''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''



original_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list=list(filter(lambda num:num%2==0,original_list))
print(even_list)
odd_list=list(filter(lambda num:num%2==1,original_list))
print(odd_list)



''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']




char6_list=list(filter(lambda word:len(word)==6,weekdays))
print(char6_list)




''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''
original_list=['orange', 'red', 'green', 'blue', 'white', 'black']
remove_words=['orange', 'black']

shortened_list=list(filter(lambda word:word not in remove_words,original_list))
print(shortened_list)





''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''

list1= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2= [2, 4, 6, 8]

new_list=list(filter(lambda num:num not in list2,list1))
print(new_list)


''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''
def search(search):
    print(list(filter(lambda word: search in word, original_list)))

search('ack')
search('abc')


''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''

def pass_check(password):
    check_list=[]
    funct=lambda function:check_list.append(function)
    funct(password.islower())
    funct(password.isupper())
    funct(password.isalpha())
    funct(len(password)<=8)
    if any(check_list)==False:
        print(f"{password} is an acceptable password")
    else:
        print(f"{password} is not an acceptable password")

str1 = "Hello8world"
pass_check(str1)
str1 = "HELLO"
pass_check(str1)
str1= "hello"
pass_check(str1)











''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''


original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
secondval=lambda key:key[1]
original_scores.sort(key=secondval)
print(original_scores)
