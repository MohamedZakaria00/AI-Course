#!/usr/bin/env python
# coding: utf-8

# Task 1: remove element thet occured more then one time 

# In[9]:


x=[ 1, 2, 3, 4, 5, 6, 7, 8, 1, 1, 1]
for x in set(x):
    
    print (x)


# Task 2: take two numbers from user and the type of operation then print the result

# In[2]:


x=int(input("Please Enter Your Frist Number "))
Operation=input("Please Enter The Type of Operantion ")
y=int(input("Please Enter Your Second Number "))
if (Operation == '+'):
    print (x+y)
elif (Operation == '-'):
    print (x-y)
elif (Operation == '*'):
    print (x*y)
elif (Operation == '/'):
    print (x/y)


# task 3 :How to print ascci reprsentation of character

# In[ ]:


o = input ("Please Enter Any Characater")
print ("The Ascii Value of "+ o +" is ", ord(o))

