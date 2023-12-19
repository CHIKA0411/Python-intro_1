#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Name-Abha Mahato regno-2241013032 sec-07
#ASSIGNMENT-2
#question-1a
x=int(input("enter a no "))
if(x%2==0):
        print(x," is even")
else:
        print(x," is odd")


# In[10]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-1b
x=str(input("enter x "))
if x[:]==x[::-1]:
    print(x,"it is palindrome")
else:
     print(x,"it is not palindrome")


# In[19]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-1c
x=str(input("enter x="))
if(x=="a"or x=="A"):
    print("vowels")
elif(x=="e"or x=="E"):
    print("vowels")
elif(x=="i"or x=="I"):
    print("vowels")
elif(x=="o"or x=="O"):
    print("vowels")
elif(x=="u"or x=="U"):
    print("vowels")
else:
    print("consonant")


# In[37]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-1d
x=str(input("enter month :"))
y=int(input("enter date :"))
#winter
if(x=="dec"):
    if(y>21):
        print("winter")
elif(x=="jan"):
        print("winter")
elif(x=="feb"):
        print("winter") 
elif(x=="mar"):
    if(y<20):
        print("winter")
#spring
if(x=="mar"):
    if(y>21 and y<32):
        print("spring")
    else:
        print("invalid input")
elif(x=="apr"):
    print("spring")
elif(x=="may"):
    print("spring") 
elif(x=="jun"):
    if(y<20 and y>0):
        print("spring")
    else:
        print("invalid input")
#summer
if(x=="jun"):
    if(y>21 and y<32):
        print("summer") 
    else:
        print("invalid input")
elif(x=="july"):
        print("summer")
elif(x=="aug"):
        print("summer") 
elif(x=="sep"):
    if(y<20 and y>0):
        print("summer")
    else:
        print("invalid input")
#fall
if(x=="sep"):
    if(y>21 and y<32):
        print("fall")  
    else:
        print("invalid input")
elif(x=="oct"):
        print("fall")
elif(x=="nov"):
        print("fall") 
elif(x=="dec"):
    if(y<20 and y>0):
        print("fall")
    else:
        print("invalid input")


# In[128]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-1e
x=int(input("enter year "))
if (x%4)==0 and (x%100)!=0 or (x%400)==0:
    
    print(x,"is a leap year")
else :
    print(x," is not a leap year")


# In[105]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-2a
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    return a / b

# Calculate the expression using the functions
result1 = 2 + 3 - 4 * 5 / 6
result2 = subtract(add(2, 3), multiply(division(5, 6), 4))

# Check if the results match
if result1 == result2:
    print("Both expressions yield the same result:", result1)
else:
    print("Results do not match.")
    
    


# In[9]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-2b
import math

def quadeq(a,b,c):
    if b*b-4*a*c>0:
        y1=-b+math.sqrt(b*b-4*a*c)/(2*a)
        y2=-b-math.sqrt(b*b-4*a*c)/(2*a)
        return (y1,y2)
    else:
        return"Imaginary roots"
print(quadeq(1,10,2))
    


# In[106]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-2c
def Hi(x):
    print("Hi", x)

# Call the function with an argument
Hi("Abha")  # Replace "Abha" with the name you want to


# In[10]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-2d
def mean(x,y,z):
    return ((x+y+z)/3)
def median(x,y,z):
        return(x+y+z-min(x,y,z)+max((x,y,z)))      
print(mean(2,3,4))
print(median(2,3,4))


# In[11]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-2e
def thesum(x):
    return (x*(x+1)/2)
print(thesum(5))


# In[137]:


#Name-Abha Mahato regno-2241013032 sec-07
#QUESTION-3
rows = 10
for i in range(0, rows+1):
    for j in range(0, rows+1 ):
        if j<=i:
            print(i*j,end=" ")
        else:
            print(j*i,end=" ")
    print()


# In[64]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-4a
rows = 4
for i in range(1, rows+1):
    for j in range(1,rows-i+1):
        print(end="  ")
    for j in range(i,0,-1):
        print(j,end=" ")
    for j in range(2,i+1):
        print(j,end=" ")
    print()


# In[60]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-4b
rows = 6
for i in range(1, rows):
    for j in range(rows-i, 0, -1):
        print(j, end=' ')
    print("")


# In[104]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-4c
rows = 4

for i in range(1, rows+1):
    for j in range(1,rows-i+1):
        print(end="  ")
    for j in range(i,0,-1):
        print("*",end=" ")
    for j in range(2,i+1):
        print("*",end=" ")
    print()
    
for i in range(rows-1,-1,-1):
    for j in range(1,rows-i+1):
        print(end="  ")
    for j in range(i,0,-1):
        print(" ",end="*")
    for j in range(2,i+1):
        print(" ",end="*")
    print()
    


# In[139]:


h = int(4)

for i in range(h):
 print(" "*(h-i),"*"*(i*2+1))
for i in range(h-2, -1, -1):
 print(" "*(h-i),"*"*(i*2+1))
 


# In[126]:





# In[ ]:





# In[ ]:




