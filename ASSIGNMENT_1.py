#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Name-Abha Mahato regno-2241013032 sec-07
#assignment 1
#question-1a
print("\"I'm a Student' of ITER.\"")


# In[2]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-1b
print("'MY Name is\n abha'")


# In[4]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-2a
print(5 and 6)


# In[ ]:





# In[5]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-2b
print(0 and 6)


# In[6]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-2c
print(0 or 1)


# In[7]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-2d
print(1 or 0)


# In[8]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-2e
print(-7*20+8/16*2+54)


# In[9]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-2f
print(5%10+10-25*8//5)


# In[10]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-2e
print("'hello'"*(5-2))


# In[11]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-2f
print("'hi'">"'hello'"or "'bye'"<"'Bye'")


# In[12]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-2g
print(10!=9 and 29!=29 and"'hi'">"'hello'" or"'bye'"<"'Bye'" and 7<=2.5)


# In[18]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-4a
marks=int(input("enter marks "))
a=300
b=400
print(marks>a and marks<b)


# In[20]:


#question-4b
grade=str(input("enter grade "))
print(grade==grade.upper())


# In[22]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-4c
exp=float(input("ENTER EXPERIENCE"))
print(exp>4.0)
print("you are eligible for job")


# In[25]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-5
length=float(input("enter length "))
width=float(input("enter width "))
area=length*width
acres=area/43560
print("area =",area,"feet")
print(acres,"in acres")


# In[26]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-6
print("enter the no.of soap")
s=int(input())
print("enter the no.of shampoo")  
sh=int(input())
p1=s*75
p2=s*111
print("price of soap=",p1)
print("price of shampoo=",p2)
p=p1+p2
print("total price=",p)


# In[28]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-7
import math
h=float(input("enter height "))
u=0.0
ag=9.8
u1=pow(u,2.0)
ad1=2.0*ag
ad=ad1*h
t=u1+ad
v=math.sqrt(t)
print("final velocity ",v)


# In[1]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-8
n=int(input("enter input"))
o=n%10
r1=n//10
o1=r1%10
r2=r1//10
o2=r2%10
r3=r2//10
o4=r3%10
print("sum of digits",o1+o2+o+o4)


# In[2]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-9
import math
print("input 3 integer")
n1=int(input())
n2=int(input())
n3=int(input())
minx=min(n1,n2,n3)
print("smallest =",minx)
maxx=max(n1,n2,n3)
print("largest=",maxx)
middle=n1+n2+n3-maxx-minx
print("middle ",middle)
print("ascending order=",minx,middle,maxx)


# In[3]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-10
import math
n1=int(input("enter days"))
n2=int(input("enter hours"))
n3=int(input("enter minutes"))
n4=int(input("enter seconds"))
seconds=n1*24*60*60+n2*60*60+n3*60+n4
print("total no. of seconds ",seconds)


# In[8]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-11
import math
r=float(input("enter radius"))
ac=math.pi*r*r
vs=4/3*math.pi*r*r
print("area of circle ",ac,"\nvolume of sphere ",vs)


# In[9]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-12
str="Hey!Hello!,Can you hear me,Mr.Hello?"
print(len(str))
print(str.upper())
print(str.lower())
print(str.title())
print(str.capitalize())
print(str.swapcase())
print(str.split(','))
print(str.find('He'))
print(str.rfind('He'))
print(str.find('He',4,12))
print(str.isalpha())
print(str.islower())
print(str.count('He'))
print(str.count('He',3,10))
print(str.startswith("Hey"))
print(str.rstrip('H'))
print(str.replace('hello','Virat'))
print(str.replace('hello','Virat',1))
print(str.endswith('!'))
print(str.partition('!'))


# In[10]:


#Name-Abha Mahato regno-2241013032 sec-07
#question-13
str="Hey!Hello!,Can you hear me,Mr.Hello?"
print(str[4:7])
print(str[:7])
print(str[4:])
print(str[-len(str):len(str)])
print(str[:-5]+str[-3:])
print('$'.join(str))


# In[ ]:




