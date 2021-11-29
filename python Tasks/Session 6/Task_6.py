#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Human:
    def __init__(self):
        self.name = ""
        self.age = ""
        self.email = ""
        self.gander = ""
        self.att = ["name","age","email","gander"]
        
    
    def addSalary(self):
        self.salary=int(input("Your Salarty is :"))
        self.updateattribute("salary")
        
        
    def updateattribute(self,attname):
        self.att.append(attname)


# In[2]:


new=Human()


# In[3]:


new.name = "Mohamed"
new.age = 21
new.gander = True
new.email = "mohamed@gmail.com"


# In[4]:


att = dict()
with open("mohamed.txt","a") as txt:
    att["name"] = new.name
    txt.writelines("name:"+str(new.name)+"\n")


# In[5]:


att


# In[6]:


new.addSalary()


# In[7]:


new.updateattribute(3000)


# In[8]:


with open("mohamed.txt","a") as txt:
    att["salary"] = new.salary
    txt.writelines("Salary:"+str(new.salary)+"\n")


# In[ ]:




