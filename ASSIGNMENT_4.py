#!/usr/bin/env python
# coding: utf-8

# Data Science Workshop-1 (CSE 2195)
# MINOR ASSIGNMENT-4: BUILT-IN DATA STRUCTURES (LIST, TUPLE, SET,
# DICTIONARY)

# What is a List Object in Python? Write the syntax, how we create a List object? For the following create List object of each scenario and display the output. (a) List of vowels. (b) List of consonants. (c) List of even integers within 1 to 20. (d) List of odd integers within 1 to 20. (e) List of all subjects in this semester. (f) List of all subject codes in this semester. (g) List of temperatures from last 10 days

# #Name-Abha Mahato regno-2241013032 sec-07
# #assignment 4
# 
# ANSWER-Lists are used to store multiple items in a single variable.
# 
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# 
# Lists are created using square[] brackets:
# thislist = ["apple", "banana", "cherry"]
# print(thislist)
# 
# -OUTPUT-
# ["apple", "banana", "cherry"]

# In[3]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#1(a) List of vowels:
vowels = ['a', 'e', 'i', 'o', 'u']
print(vowels)


# In[4]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#1(b) List of consonants:
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
print(consonants)


# In[5]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#1(c) List of even integers within 1 to 20:
even_numbers = [x for x in range(2, 21, 2)]
print(even_numbers)


# In[6]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#1(e) List of all subjects in this semester:
subjects = ['Probability and Statistics', 'Principle of Economics', 'Data Science workshop-I', 'Algorithms Design', 'Digital Logic Design']
print(subjects)


# In[7]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#1(f) List of all subject codes in this semester:
subject_codes = ['MTH2002','HSS2021','CSE2195','CSE3131','EET1211']
print(subject_codes)


# In[8]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#1(g) List of temperatures from the last 10 days:
temperatures = [28.5, 30.1, 29.7, 27.8, 26.3, 31.2, 29.9, 28.4, 30.5, 27.2]
print(temperatures)


# 2. Predict the output of following instructions when typed in Jupyter Notebook Cell and note down every output in your assignment copy.

# In[12]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#2A
listObj = range(15)
print(listObj)
print(list(listObj))


# In[13]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#2B
someList = ["Bob", "Joe", "Will", 55, "Will", "XXXXX", 100.55]
print(type(someList))
print(someList[0])
print(someList[-1])
print(someList[3])
print(someList[-3])
print(someList[2])
print(someList[2:5])
print(someList[-4:-1])
print(someList[:5])
print(someList[2:])
print(someList[:])
print(someList[0:6:2])
print(someList[::2])
print(someList[::-1])
print(someList[1:5:2])


# In[17]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#2C
list1 = [2, 3, 7, None]
list2 = ["foo", "bar", "baz"]
list2 = list1
list2[2] = "SampleText"
print(list1)
print(list1[2])
print(list2[2])
print(list2)
print()


# In[19]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#2d
wordList = ['foo', 'bar', 'baz']
wordList[2] = "peekaboo"
print(wordList)
print(wordList.append("dwarf"))
print(wordList)
print(wordList.insert(1, "red"))
print(wordList)
print(wordList.pop(2))
print(wordList)
print(wordList.append("foo"))
print(wordList)
wordList.remove("foo")
print(wordList)
print("dwarf" in wordList)
print("dwarf" not in wordList)


# In[22]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#2e
print([4, None, "foo"] + [7, 8, 2, 3])
list1 = [4, None, "foo"] + [7, 8, 2, 3]
print(list1)
x = ['A', ('B', 'C')]
print(x.extend(list1))
print(x)
print(list1)
a = [7, 2, 5, 1, 3, 73, 51, 7, 3, 9, 11, 1, 1, 10, 9]
print(a)
print(a.sort())
print(a)
b = ["saw", "small", "He", "foxes", "six"]
print(b.sort(key=len))
print(b)
print(b.sort())
print(b)


# 3. Develop Python Programs for the following below scenario.
# (a) Write a Python Program which will prompt user to ask a range of integer(lower limit and higher limit) value. Once you receive the input values from the user programmatically store odd numbersand even numbers into separate list objects and display them as output.

# In[23]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#3a
lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

odd_numbers = []
even_numbers = []

for num in range(lower_limit, upper_limit + 1):
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)


# (b) Write a Python Program which will prompt user to enter a positive integer value. Once you receive
# the input, find factors of the integer and store into a list objects and display them as output.

# In[24]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#3b
number = int(input("Enter a positive integer: "))

factors = [x for x in range(1, number + 1) if number % x == 0]

print("Factors of", number, "are:", factors)


# (c) Program to separate prime and composite numbers from a given range:

# In[25]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#3c
lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

prime_numbers = []
composite_numbers = []

for num in range(lower_limit, upper_limit + 1):
    if num < 2:
        continue
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)
    else:
        composite_numbers.append(num)

print("Prime numbers:", prime_numbers)
print("Composite numbers:", composite_numbers)


# 4. What is a Tuple Object in Python? Write the syntax, how we create a Tuple object? For the following
# scenario create Tuple object of each scenario and display them as output.
# (a) Tuple of few student’s information such as roll number, name, branch, specialization, mobile,
# email id etc.
# (b) Tuple of few book’s information such as ISBN Number, book title, category, author, number of
# authors etc.
# (c) Tuple of few parts of a vehicle.
# (d) Tuple of few institution details such as name of the institute, departments, no. of students, address
# etc.
# (e) Create tuple objects from List objects at all scenario in Question No. 1.

# ANSWER-A tuple is a built-in data structure in Python that is similar to a list but is immutable, meaning its elements cannot be changed after creation. Tuples are defined using parentheses () and the elements within a tuple are separated by commas.

# my_tuple = (item1, item2, item3, ...)

# In[29]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#4A  Tuple of student's information:
student1_info = (2241013032, "ABHA MAHATO", "CSE", "DATA SCIENCE", "9031490620", "abhamahato2004@gmail.com")
print(student1_info)
student2_info = (2241011211, "VIVEK KUMAR", "CSE", "CORE", "9162619621", "vivek.kr51556@gmail.com")
print(student2_info)


# In[30]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#4b  Tuple of book's information:
book_info = ("ISBN123456", "Python Programming", "Programming", "John Smith", 1)
print(book_info)


# In[31]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#4c) Tuple of parts of a vehicle: 
vehicle_parts = ("Engine", "Wheels", "Brakes", "Transmission", "Suspension")
print(vehicle_parts)


# In[32]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#4(d) Tuple of institution details:
institution_details = ("ITER SOA", ["Computer Science", "Electrical Engineering","Computer Science And Information technology","Mechnical Engineering","Civil Enginnering"], 7000, "BHUBANSAWER")
print(institution_details)


# In[34]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#4(e) Create Tuple objects from List objects in Question No. 1:
#4(e.1) Tuple of vowels:
vowels_list = ['a', 'e', 'i', 'o', 'u']
vowels_tuple = tuple(vowels_list)
print(vowels_tuple)


# In[35]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#4(e.2) Tuple of consonants:
consonants_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
consonants_tuple = tuple(consonants_list)
print(consonants_tuple)


# In[36]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#(e.3) Tuple of even integers within 1 to 20:
even_numbers_list = [x for x in range(2, 21, 2)]
even_numbers_tuple = tuple(even_numbers_list)
print(even_numbers_tuple)


# In[38]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#(e.4) Tuple of odd integers within 1 to 20:
odd_numbers_list = [x for x in range(1, 21, 2)]
odd_numbers_tuple = tuple(odd_numbers_list)
print(odd_numbers_tuple)


# In[41]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#(e.5) Tuple of subjects in this semester:
subjects_list = ['Probability and Statistics', 'Principle of Economics', 'Data Science workshop-I', 'Algorithms Design', 'Digital Logic Design']
subjects_tuple = tuple(subjects_list)
print(subjects_tuple)


# In[42]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#(e.6) Tuple of subject codes in this semester:
subject_codes_list = ['MTH2002','HSS2021','CSE2195','CSE3131','EET1211']
subject_codes_tuple = tuple(subject_codes_list)
print(subject_codes_tuple)


# In[43]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#(e.7) Tuple of temperatures from the last 10 days:
temperatures_list = [28.5, 30.1, 29.7, 27.8, 26.3, 31.2, 29.9, 28.4, 30.5, 27.2]
temperatures_tuple = tuple(temperatures_list)
print(temperatures_tuple)


# 5. Predict the output of following instructions when typed in Jupyter Notebook Cell and note down every output in your assignment copy.

# In[44]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#5a)
tupleObj = (4, 5, 6, "Abha", "Mahato", 120.5643)
print(tupleObj)
print(type(tupleObj))
print(tuple((2, 5, 1, 9, 5, 3, 8)))
print(tuple((4, 5, 6)))
x = tuple([2, 5, 1, 9, 5, 3, 8])
print(x)
y = x
print(type(y))
tupleObj = tuple('string')
print(tupleObj)


# In[45]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#5b)
someList = ["Bob", "Joe", "Will", 55, "Will", "XXXXX", 100.55]
someTuple = tuple(someList)
print(type(someTuple))
print(someTuple[0])
print(someTuple[-1])
print(someTuple[3])
print(someTuple[-3])
print(someTuple[2])
print(someTuple[2:5])
print(someTuple[-4:-1])
print(someTuple[:5])
print(someTuple[2:])
print(someTuple[:])
print(someTuple[0:6:2])
print(someTuple[::2])
print(someTuple[::-1])
print(someTuple[1:5:2])


# In[49]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#5c
nestedTuple = (4, 5, 6), (7, 8)
print(nestedTuple)
print(nestedTuple[1])
tup = tuple(['foo', [1, 2], True])
print(tup[1].append(3))
print(tup)
print(list2)
tup[2] = False


# In[51]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#5d
tup = (4, 5, 6)
a, b, c = tup
print(b)
tup = 4, 5, (6, 7)
a, b, (c, d) = tup
print(d)
a, b = 1, 2
a, b = b, a
print(a)
print(b)
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    print(f'a=a, b=b, c=c')
values = 1, 2, 3, 4, 5
a, b, *rest = values
print(a)
print(b)
print(rest)


# In[55]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#5e
print((4, None, 'foo') + (6, 0) + ('bar',))
tuple1 = (4, None, 'foo') + (6, 0) + ('bar',)
print(tuple1)
print(('foo', 'bar') * 4)
a = (1, 7, 2, 7, 2, 2, 7, 3, 7, 4, 7, 7, 2, 7)
print(a.count(7))
print(len(a))


# In[56]:


#Name-Abha Mahato regno-2241013032 sec-07 
#assignment 4
#6(a) Prompting the user to enter personal details and storing them in tuple objects:
user_details = []

for _ in range(5):  # Collect details for 5 users
    name = input("Enter your name: ")
    department = input("Enter your department: ")
    mobile_number = input("Enter your mobile number: ")
    roll_number = input("Enter your roll number: ")
    user_info = (name, department, mobile_number, roll_number)
    user_details.append(user_info)

for user_info in user_details:
    print("Name:", user_info[0])
    print("Department:", user_info[1])
    print("Mobile Number:", user_info[2])
    print("Roll Number:", user_info[3])


# In[59]:


#6b(a) Storing odd and even numbers in separate tuple using list objects:
lower_limit = int(input("Enter lower limit: "))
upper_limit = int(input("Enter upper limit: "))

even_numbers = [x for x in range(lower_limit, upper_limit + 1) if x % 2 == 0]
odd_numbers = [x for x in range(lower_limit, upper_limit + 1) if x % 2 != 0]
even_numbers_tuple=tuple(even_numbers)
odd_numbers_tuple=tuple(odd_numbers)
print("Even Numbers:", even_numbers_tuple)
print("Odd Numbers:", odd_numbers_tuple)


# In[62]:


#6b(b)Finding factors of a positive integer and storing them in a  tuple using list object:
number = int(input("Enter a positive integer: "))
factors = [x for x in range(1, number + 1) if number % x == 0]
factors_tuple=tuple(factors )
print("Factors of", number, "are:", factors_tuple)


# In[65]:


#6b(c)Listing prime and composite numbers in a given range using tuple in list objects:
lower_limit = int(input("Enter lower limit: "))
upper_limit = int(input("Enter upper limit: "))

prime_numbers = []
composite_numbers = []

for num in range(lower_limit, upper_limit + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                composite_numbers.append(num)
                break
        else:
            prime_numbers.append(num)
prime_numbers_tuple=tuple(prime_numbers)
composite_numbers_tuple=tuple(composite_numbers)
print("Prime Numbers:", prime_numbers_tuple)
print("Composite Numbers:", composite_numbers_tuple)


# 7. What is a Dictionary Object in Python? Write the syntax, how we create a Dictionary object? For
# the following questions create Dictionary object of each scenario and display them as output.
# (a) Dictionary of few peoples as key and their mobile numbers as values(at least for 10 key).
# (b) Dictionary of few books as key and their authors(authors should be a list object) as values.
# (c) Dictionary of different types numbers(such as prime, composite, even, odd etc.) as keys and their
# examples as values.
# (d) Dictionary of engineering branches as keys and their specializations as values.
# (e) Dictionary of employee ids as keys and their details(as tuple) as values.
# (f) Dictionary of subject code as key and subject details(as list) such as course name, reference book,
# teacher name, department etc. as values.
# 
# 

# ANSWER-A dictionary in Python is a collection of key-value pairs, where each key is associated with a value. The syntax for creating a dictionary is as follows:

# my_dict = {
#     "key1": "value1",
#     "key2": "value2",
#     "key3": "value3",
#     # ...
# }
# 

# In[67]:


people_mobile_dict = {
    "Abha": "123-456-7890",
    "Bina": "987-654-3210",
    "Ck": "555-123-4567",
    # Add more entries
}
print(people_mobile_dict)



# In[68]:


books_authors_dict = {
    "DS": ["abha"],
    "Book2": ["Author2", "Author3"],
    "Book3": ["Author4"],
    # Add more entries
}
print(books_authors_dict)


# In[69]:


numbers_dict = {
    "Prime": [2, 3, 5, 7, 11],
    "Composite": [4, 6, 8, 9, 10],
    "Even": [2, 4, 6, 8, 10],
    "Odd": [1, 3, 5, 7, 9],
}
print(numbers_dict)


# In[70]:


engineering_dict = {
    "Mechanical": ["Thermodynamics", "Mechatronics", "Automotive Engineering"],
    "Electrical": ["Power Systems", "Electronics", "Control Systems"],
    "Computer Science": ["Machine Learning", "Software Engineering", "Data Science"],
    # Add more entries
}
print(engineering_dict)


# In[71]:


employee_details_dict = {
    "ID001": ("John Doe", "Engineering", "Senior Engineer"),
    "ID002": ("Alice Smith", "Marketing", "Marketing Manager"),
    "ID003": ("Bob Johnson", "Finance", "Accountant"),
    # Add more entries
}
print(employee_details_dict)


# In[17]:


subject_details_dict = {
    "CS101": ["Introduction to Programming", "Python for Beginners", "Dr. Smith", "Computer Science"],
    "ENG202": ["Advanced Mechanical Engineering", "Mechanical Systems", "Prof. Johnson", "Mechanical Engineering"],
    # Add more entries
}
print(subject_details_dict)


# 8. Predict the output of following instructions when typed in Jupyter Notebook Cell and note down every
# output in your assignment copy.

# In[16]:


#a
dictObj = {"fruits": ["banana", "apple", "guava", "jackfruit"], "colors": ("red", "blue", "green"),
"int": 165, "float": 99.56, "string":"some sample text"}
print(dictObj)
print(type(dictObj))
print({"key":"value"})
dictObj[10] = "New added value"
print(dictObj)
print(dictObj[10])
print(dictObj["int"])
print(dictObj["colors"])
print(dictObj[10])
#print(dictObj['10']) key error


# In[15]:


#b
dictObj2 = {"Bob":10, "Joe":34, "Will":77, "Limba":55, "Will":36, "XXXXX":100}
print("Limba" in dictObj2)
print(55 in dictObj2)
print("55" in dictObj2)
print("XXXXXX" in dictObj2)
dictObj2["Will"] = ' '.join(["I", "am", "ancient", "10", "years old"])
print(dictObj2["Will"])
# dictObj2.pop() expect an argument
print(dictObj2.pop("Will"))
print(dictObj2)


# In[8]:


#c
dictObj = {"fruits": ["banana", "apple", "guava", "jackfruit"], "colors": ("red", "blue", "green"),
"int": 165, "float": 99.56, "string":"some sample text"}
list(dictObj.keys())
list(dictObj.values())
list(dictObj.items())
dictObj["iter"] = "INSTITUTE OF TECHNICAL EDUCATION & RESEARCH"
list(dictObj.keys())
list(dictObj.values())
list(dictObj.items())
dictObj
dictObj.update({'b':"foo",'c':12})
dictObj


# In[1]:


# d
myDict = {}
keyList = range(10)
valueList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'G', 'I', 'J']
for key, value in zip(keyList, valueList):
    myDict[key] = value
myDict


# In[2]:


#e
from collections import defaultdict
words = ["duck","apple","dog","bat","cat","cup","bar","atom","book","dance"]
myDict = defaultdict(list)
for w in words:
    myDict[w[0]].append(w)
myDict


# 9. Develop Python Programs for the following below scenario.
# (a) Write a Python Program which will prompt user to ask enter his/her name, profession, mobile
# number, employment organization, email id etc. Once you receive the input values from the user
# programmatically store these values into Dictionary objects such as mobile number is the key and
# other details as tuple object. Try to enter details for at least 7 objects.
# (b) Develop a Python program which will take lower limit +ve integer and higher limit +ve integer
# values from the user as user input(lower limit should be lesser than the higher limit). Following
# that calculate factors of those elements within the range and store them as key value pairs(dictionary
# object) such as the number is the key and factors are as values of a list object and display them.
# (c) Modify the Question No. (a) to develop a Python program which will consider name as the key
# and rest values into tuple as the value. Without using any predefined sort() method use your own
# logic to sort them based on name and finally display them as output.

# In[19]:


#9A
user_details = {}  # Create an empty dictionary to store user details

# Prompt the user to enter details for 7 objects
for i in range(2):     #we can replace 2by 7 in order to take 7 input
    name = input("Enter your name: ")
    profession = input("Enter your profession: ")
    mobile_number = input("Enter your mobile number: ")
    organization = input("Enter your employment organization: ")
    email = input("Enter your email id: ")
    
    # Store the details in a tuple
    user_info = (name, profession, organization, email)
    
    # Use the mobile number as the key in the dictionary
    user_details[mobile_number] = user_info

# Display the dictionary with user details
print(user_details)


# In[83]:


#9B
lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

if lower_limit >= upper_limit:
    print("Lower limit should be less than the upper limit.")
else:
    factors_dict = {}  # Create an empty dictionary to store factors
    
    for num in range(lower_limit, upper_limit + 1):
        factors = [i for i in range(1, num + 1) if num % i == 0]
        factors_dict[num] = factors
    
    # Display the dictionary with factors
    print(factors_dict)


# In[ ]:


#9C
user_details = {}  # Create an empty dictionary to store user details

# Prompt the user to enter details for 7 objects
for i in range(7):
    name = input("Enter your name: ")
    profession = input("Enter your profession: ")
    mobile_number = input("Enter your mobile number: ")
    organization = input("Enter your employment organization: ")
    email = input("Enter your email id: ")
    
    # Store the details in a tuple
    user_info = (name, profession, organization, email)
    
    # Use the name as the key in the dictionary
    user_details[name] = user_info

# Display the dictionary with user details
print(user_details)


# 10. What is a Set Object in Python? Write different syntax, how we create a Set object? For the following
# questions create Set object of each scenario and display them as output.
# (a) Set of all cricket players currently working in Indian Cricket Team.
# (b) Set of all 3rd semester courses.
# (c) Set of all books you are following for this semester.
# (d) Set of 10 integer objects(both -ve and +ve) which are divisible by 11.
# (e) Set of words containing more than 3 vowels.

# A set in Python is an unordered collection of unique elements. Here's the syntax for creating a set object:

# my_set = {element1, element2, element3, ...}

# In[85]:


#(a) Set of all cricket players currently working in the Indian Cricket Team:
indian_cricket_team = {"Virat Kohli", "Rohit Sharma", "Jasprit Bumrah", "Cheteshwar Pujara" }
print(indian_cricket_team)


# In[86]:


third_semester_courses = {"Mathematics 301", "Computer Science 302", "Physics 303"}
print(third_semester_courses)


# In[87]:


semester_books = {"Python Programming", "Data Structures and Algorithms", "Physics for Engineers"}
print(semester_books)


# In[88]:


divisible_by_11 = {-22, -11, 0, 11, 22, 33, 44, 55, 66, 77}
print(divisible_by_11)


# In[89]:


vowel_words = {"education", "extraordinary", "unbelievable", "adventure", "communication", ...}
print(vowel_words)


#  11.Predict the output of following instructions when typed in Jupyter Notebook Cell and note down everyoutput in your assignment copy.

# In[31]:


#a
A = {5, 3, 1, 4, 4, 2, 3, 4, 5, "5", 2, "2", 7, "1"}
print(A)
B = {"6", 3, 1, 3, "5", "2", 7, "1", 6, "9", 10, 9, "6"}
print(B)
print(type(A))
print(type(B))
print(A.add("55"))
print(A)
D = B
print(D)
print(D == B)
print(D == A)
#b
C = A
print(C.union(D))
print(C)
print(C.intersection(D))
print(C)
print(D)
print(C.intersection_update(D))
print(C)
print(D)
print(C.update(D))
print(C)
#c
print(C.add(54))
print(C)
print(C.add("Sample Text"))
print(C)
print(D)
print(C.difference(D))
print(C)
print(D)
print(C.difference_update(D))
print(C)
print(D)
#D
print(C.symmetric_difference(D))
print(C)
print(C.symmetric_difference_update(D))
print(C)
print(A.issubset(B))
print(A.issuperset(B))
print(A)
print(B)
#E
X = {1, 2, 3, 4, 2, 3, 5, 6, 1, 2, 9, 8}
print(X)
Y={''}
print(Y.add(100.65))
print(Y.add("ITER"))
print(Y.add(76.89))
print(Y)
print(Y| X)
print(Y & X)
#print(Y-X) not found such bit wise operator
print(Y^X)
print(Y)
print(X)
#Y | = X not there is no such conditional bitwise  operator
#Y & = X not there is no such conditional bitwise  operator
print(Y)
print(X)




# 12. Develop Python Programs for the following below scenario.
# (a) Write a Python Program which will prompt user to enter 10 different sample inputs like integer/float/string/boolean/list/tuple/set/dictionary objects etc. and store them into a Set object. Find
# out all unique characters present in that set object.
# (b) Develop a Python program which will prompt user to enter 15 positive numbers randomly(repetition
# allowed) and divide all those unique numbers into two different list objects such that one list contains prime numbers and another list contains composite numbers. Finally, display the output.
# (c) Develop a Python script which will prompt the user to enter 10 student details such as roll number, name, Physics Mark, Chemistry Mark, Mathematics mark as tuple objects and display them.
# Finally update those student details with adding fields such as total mark, average mark, status(pass
# if average mark is > 60) by adding student details as list of tuples and display the outp

# In[91]:


#12A
# Initialize an empty set
unique_set = set()

# Prompt the user for 10 different inputs
for _ in range(10):
    user_input = input("Enter a value: ")
    unique_set.add(user_input)

# Find unique characters
unique_characters = set()
for item in unique_set:
    unique_characters.update(set(item))

print("Unique characters in the input:", unique_characters)


# In[95]:


#12B
# Initialize lists for prime and composite numbers
prime_numbers = []
composite_numbers = []

# Prompt the user for 15 positive numbers (repetitions allowed)
for _ in range(15):
    user_input = int(input("Enter a positive number: "))
    if user_input < 2:
        print("Number must be greater than 1. Skipping...")
        continue

    is_prime = True
    for i in range(2, int(user_input**0.5) + 1):
        if user_input % i == 0:
            is_prime = False
            break

    if is_prime:
        prime_numbers.append(user_input)
    else:
        composite_numbers.append(user_input)

print("Prime numbers:", prime_numbers)
print("Composite numbers:", composite_numbers)


# In[1]:


#12C
# Initialize a list to store student details as tuples
students = []

# Prompt the user for 10 student details
for x  in range(1)://we can replace 1 by 10 in in order to collect data for 10 student
    roll_number = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    physics_mark = float(input("Enter Physics Mark: "))
    chemistry_mark = float(input("Enter Chemistry Mark: "))
    mathematics_mark = float(input("Enter Mathematics Mark: "))

    total_mark = physics_mark + chemistry_mark + mathematics_mark
    average_mark = total_mark / 3
    status = "Pass" if average_mark > 60 else "Fail"

    student_details = (roll_number, name, physics_mark, chemistry_mark, mathematics_mark, total_mark, average_mark, status)
    students.append(student_details)

# Display student details
for student in students:
    print("Student Details:", student)


# In[ ]:




