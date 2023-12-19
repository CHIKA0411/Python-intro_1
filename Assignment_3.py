#!/usr/bin/env python
# coding: utf-8

# Data Science Workshop-1 (CSE 2195)
# ASSIGNMENT-3: FUNCTIONS, CONTROL STRUCTURES(PART II)
# 1. In a particular jurisdiction, old format of license plates consist of three uppercase letters followed by three digits and new format consist of four digits followed by three uppercase letters. Write a program that begins by reading a string of characters from the user. Then your program should display a message indicating whether the characters are valid for an old style license plate or a new style license plate

# In[2]:


#Name-Abha Mahato regno-2241013032 sec-07
#assignment 3
PLATE=input('enter a no. plate')
def is_old_style_plate(plate):
    if len(plate) == 6:
         if plate[:3].isalpha() and plate[:3].isupper():
                 if plate[3:].isdigit():
                        return True
    return False
def is_new_style_plate(plate):
    if len(plate) == 7:
         if plate[:4].isdigit():
                if plate[4:].isalpha() and plate[4:].isupper():
                    return True
    return False
if is_old_style_plate(PLATE):
    print("Valid old-style license plate ", PLATE)
elif is_new_style_plate(license_plate):
    print("Valid new-style license plate ", PLATE)
else:
    print("Invalid license plate format ", PLATE)


# 2. Check whether a string is palindrome or not(Without using inbuilt functions.)

# In[6]:


#Name-Abha Mahato regno-2241013032 sec-07
#assignment 3
#check palindrome w/o using string slicing
#methord-1
s=str(input("enter the string "))
r=""
flag=0
for i in range(len(s)//2):
    if s[i]!=s[-(i+1)]:
        flag=1
    
if(flag==1):
     print("string is not palindrome ",s)
else:
    print("string is palindrome ",s)


# 3. Write a program that reads two positive integers from the mine and report their greatest common divisor

# In[7]:


#Name-Abha Mahato regno-2241013032 sec-07
#assignment 3
#gcd
x=int(input("Enter a number1:"))
y=int(input("Enter a number2:"))
def gcd(x,y):
    if y>x:
        x,y=y,x
    while(y>0):
        x,y=y,x%y
        if y==0:
            return x
print("GCD =",x)


# 4. Write a program that reads an integer from the user and displays a message indicating whether or not it is prime.

# In[9]:


#Name-Abha Mahato regno-2241013032 sec-07
#assignment 3
#prime no.
n=int(input("enter the no."))
flag=0
for i in range(2,n):
    if n%i==0:
        flag=flag+1
        break
if(flag==0):
    print("the no. is prime ",n)
else:
    print("the no. is not prime ",n)
    


# 5. Write a function that determines whether or not a password is good. We will define a good passwordto be a one that is at least 8 characters long and contains at least one uppercase letter, at least onelowercase letter, and at least one number.

# In[3]:


#Name-Abha Mahato regno-2241013032 sec-07
#assignment 3
def is_good_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True
user_password = input("Enter a password: ")
if is_good_password(user_password):
    print("Good password!")
else:
    print("Password does not meet the criteria.")


# 6. Write a program to input 10 numbers. Then compute and display the sum of even numbers and product of odd numbers.

# In[10]:


#Name-Abha Mahato regno-2241013032 sec-07
#assignment 3
#10 input check if even or odd find the sum and product of odd no.
n=10
se=0
po=1
for i in range(1,n+1):
    n1=int(input("enter the no. "))
    if(n1%2==0):
        print("the no is even ")
        se=se+n1
    elif(n1%2==1):
        print("the no is odd")
        po=po*n1
print("the sum of even no. ",se)
print("the product of odd no. ",po) 


# 7. Write a program to compute the factorial of a number

# In[28]:


#Name-Abha Mahato regno-2241013032 sec-07
#assignment 3
#question-7 factorial of the no
n=int(input("enter a no."))
fact=1
if n>0:
    for i in range(1,n+1):
        fact=fact*i
    print("factorial of this no.is ",fact)
elif n==0:
    print("factorial of this no.is ",0)
elif n<0:
    print("invalid input")


# 8. Write a Python Program to Count the Number of Occurrence of a Character in String, without using str.count() method.

# In[5]:


#Name-Abha Mahato regno-2241013032 sec-07
#assignment 3
def count_char_occurrences(string,counter):
    count = 0
    for char in string:
        if char == counter:
            count += 1
    return count
user = input("Enter a string: ")
count = input("Enter a character to count: ")
if len(count) == 1:
    o = count_char_occurrences(user,count)
    print(f"The character '{count}' appears {o} times in the string.")
else:
    print("Please enter a single character for counting.")


# 9. Write a program to generate prime numbers in a certain range input by the user. if (number break else: print (number)

# In[6]:


#Name-Abha Mahato regno-2241013032 sec-07
#assignment 3
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
def generate_primes_in_range(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)
# Take user input for the range
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
print("Prime numbers in the range:")
generate_primes_in_range(start, end)


# 10. Write a program to reverse the digits of a number.(You should not use any string methods.)

# In[24]:


#Name-Abha Mahato regno-2241013032 sec-07
#assignment 3
#find the reverse of a given number
n=int(input("Enter a number:"))
x=0
while(n>0):
    x=(x*10)+(n%10)
    n=n//10
print("the reverse of this no: ",x)


# 11. Write a program to determine an Armstrong number

# In[23]:


#Name-Abha Mahato regno-2241013032 sec-07
#assignment 3
def check_armstrong(n):
    n=int(input("Enter a num"))
    p=len(str(n))
    temp=n
    x=0
    while n>0:
        x+=(n%10)**p
        n=n//10
    if(temp==x):
        print("the given no. is a Armstrong no",temp)
    else:
        print("the given no. is not a Armstrong no",temp)
check_armstrong(n)


# 12. Write a program that prompts the user for an integer number and then prints all it’s factors

# In[22]:


#Name-Abha Mahato regno-2241013032 sec-07
#assignment 3
#print factors
n=int(input("Enter a num"))
print("the fators of num are")
def printing_factor(n):
    for i in range(1,n+1):
        if(n%i==0):
            print(i)
printing_factor(n)


# 13. Write a program that prompts a number from the user and generates the Fibonacci sequence up to that number. The Fibonacci sequence is given as under: 0, 1, 1, 2, 3, 5, 8

# In[21]:


#Name-Abha Mahato regno-2241013032 sec-07
#assignment 3
#fibonacci
n=int(input("Enter  the no iteration "))
print("the fibonacci series")
def fibonacci(n):
    a=0
    b=1
    print(a)
    while b<n:
        print(b)
        a,b=b,a+b
fibonacci(n)


# 14. Write a python program to find the area of a triangle whose three sides are given.

# In[7]:


#Name-Abha Mahato regno-2241013032 sec-07
#assignment 3
import math
def calculate_area_of_triangle(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
# Take user input for the lengths of the three sides
a = float(input("Enter the length of side 'a': "))
b = float(input("Enter the length of side 'b': "))
c = float(input("Enter the length of side 'c': "))
if a + b > c and a + c > b and b + c > a:
    area = calculate_area_of_triangle(a, b, c)
    print(f"The area of the triangle is {area:.2f} square units.")
else:
    print("The input sides cannot form a valid triangle.")


# 15. Write a python program to find out the average of a set of integers

# In[9]:


#Name-Abha Mahato regno-2241013032 sec-07
#assignment 3
input_numbers = input("Enter a set of integers separated by spaces: ")
numbers = input_numbers.split()
total = 0
count = 0
for num in numbers:
    try:
        num = int(num)
        total += num
        count += 1
    except ValueError:
        print(f"Skipping invalid input: {num}")
if count > 0:
    average = total / count
    print(f"The average of the numbers is: {average:.2f}")
else:
    print("No valid numbers provided.")


# 16. Write a python program to find the sum of the digits of an integer using a while loop

# In[11]:


#Name-Abha Mahato regno-2241013032 sec-07
#assignment 3
num = int(input("Enter an integer: "))
if num < 0:
    num = abs(num)
total = 0
temp_num = num
while temp_num > 0:
    digit = temp_num % 10
    total += digit
    temp_num //= 10
print(f"The sum of the digits in {num} is: {total}")


# 17. Write a python program to display all integers within the range 100-200 whose sum of digits is an even number

# In[20]:


#Name-Abha Mahato regno-2241013032 sec-07
#assignment 3
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total
print("Integers with an even sum of digits in the range 100-200:")
for num in range(100, 201):
    if sum_of_digits(num) % 2 == 0:
        print(num)


# 18. Write a python program that takes two numbers as input parameters and returns True or False depending on whether they are co-primes. Two numbers are called co-prime if they don’t have any common divisor other than one.

# In[17]:


#Name-Abha Mahato regno-2241013032 sec-07
#assignment 3
x=int(input("Enter a number1:"))
y=int(input("Enter a number2:"))
def gcd(x,y):
    if y>x:
        x,y=y,x
    while(y>0):
        x,y=y,x%y
        if y==0:
            return x
def co_prime(x,y):
    if(gcd(x,y)==1):
        print(x, " and ",y," coprime")
    else:
        print(x, " and ",y," not coprime")
co_prime(x,y)


# 19. (FizzBuzz Game in Python)Assume you are given the number ’n,’ and asked to display the stringrepresentations of all the numbers from 1 to n. However, there are some restrictions, such as:
# – If the number can be divided by 3, it will output Fizz instead of the number.
# – If the number is divisible by 5, the result will display Buzz instead of the number.
# – If the given number is divisible by both 3 and 5, Fizz Buzz will be printed instead of the number.
# – If the number cannot be divided by 3 or 5, it will be printed as a string.

# In[26]:


#Name-Abha Mahato regno-2241013032 sec-07
#assignment 3
def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(str(i))

# Take user input for 'n'
n = int(input("Enter a number 'n': "))
fizz_buzz(n)


# 20. (Rock-Paper-Scissor)Create a simple command-line Rock-Paper-Scissor game without using any external game libraries like PyGame. In this game, the user gets the first chance to pick the option between Rock, paper, and scissors. After the computer select from the remaining two choices(randomly),
# the winner is decided as per the rules.
# – Rock smashes scissors.(Rock wins over scissors)
# – Paper covers rock.(Paper wins over Rock)
# – Scissors cut paper.(Scissors win over paper

# In[14]:


#Name-Abha Mahato regno-2241013032 sec-07
#assignment 3
import random

# Function to get user choice
def get_user_choice():
    user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid choice. Enter 'Rock', 'Paper', or 'Scissors': ").lower()
    return user_choice

# Function to get computer choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        return f"You win! {user_choice} beats {computer_choice}."
    else:
        return f"Computer wins! {computer_choice} beats {user_choice}."

# Main game loop
while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")
    result = determine_winner(user_choice, computer_choice)
    print(result)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break


# *21. (Coin flip simulation) What’s the minimum number of times you have to flip a coin before you can have three consecutive flips that result in the same outcome (either all three are heads or all three are tails)? How many flips are needed on average?(Experiment by doing the experiment for 10 times).
# Display an H each time the outcome is heads, and a T each time the outcome is tails, with all of the outcomes for one simulation on the same line. Then display the number of flips that were needed to reach 3 consecutive occurrences of the same outcome.

# In[15]:


#Name-Abha Mahato regno-2241013032 sec-07
#assignment 3
import random

def simulate_coin_flips():
    flips = ""
    count = 0
    consecutive_count = 0
    current_outcome = None

    while consecutive_count < 3:
        flip = random.choice(['H', 'T'])
        flips += flip
        count += 1

        if flip == current_outcome:
            consecutive_count += 1
        else:
            consecutive_count = 1
            current_outcome = flip

    return flips, count

# Perform the experiment 10 times
for _ in range(10):
    flips, count = simulate_coin_flips()
    print(flips, f"({count} flips)")

# Calculate the average number of flips needed
total_flips = sum(simulate_coin_flips()[1] for _ in range(10))
average_flips = total_flips / 10
print(f"Average number of flips needed: {average_flips:.2f}")


# *22. (Guessing game problem) Write a program to select a random number between 1 and 10 and the user
# has to guess it in 5 attempts. Based on the user’s guess computer will give various hints if the number
# is high or low. When the user guess matches the number computer will print the answer along with
# the number of attempts.

# In[16]:


#Name-Abha Mahato regno-2241013032 sec-07
#assignment 3
# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

attempts = 0

# Main game loop
while attempts < 5:
    guess = int(input("Guess the number (between 1 and 10): "))
    attempts += 1

    if guess < random_number:
        print("The number is higher.")
    elif guess > random_number:
        print("The number is lower.")
    else:
        print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")
        break

if attempts == 5:
    print(f"Sorry, you've used all your attempts. The number was {random_number}.")


# In[ ]:




