#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task2: implement unorderdset usenig list
l=[1,1,2,3,2,6,3,2,4,5,7,6,9,8,41,23,5,2,1]
unorderset= list(dict.fromkeys(l))
print(unorderset)


# In[2]:


#Task3: implement binary search so that when searching return either the right index or not found
def binarySearch (arr, l, i, x):
    if i >= l: 
        mid = l + (i - l) // 2
 
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, i, x)
 
    else:
        return -1

arr = [ 1 ,2, 3, 4, 10, 11, 15, 40 ]
x = 11
 
result = binarySearch(arr, 0, len(arr)-1, x)
 
if result != -1:
    print (result)
else:
    print ("Element is not present in array")

