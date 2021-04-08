#!/usr/bin/env python
# coding: utf-8

# #  Array
# 

# 1.array is an object that provide a mechaanism for storing several data in one identifier.array is used to store group of data in same data type
# 2.In python size of array is not fixed array can increase or decrease their size dynamically
# 3.array is not same as list
# 4.array use less sapace than list
# 

# # Types of array

# 2 types
# 1.one dimensional
# 2.multi dim, but python not support 2d but by the help of numpy we use it
# 

# In[2]:


import array


# In[6]:


arr = array.array('i', [1, 2, 3])
arr


# In[10]:


##append,insert
arr = array.array('i', [1, 2, 3])
 
print ("The new created array is : ",end=" ")
for i in range (0, 3):
    print (arr[i], end=" ")
print("\n")

arr.append(4)                                  #append
print("The appended array is : ", end="")
for i in range (0, 4):
    print (arr[i], end=" ")
print("\n")

arr.insert(2, 5)                                 #insert
print ("The array after insertion is : ", end="")
for i in range (0, 5):
    print (arr[i], end=" ")


# In[15]:


#pop,remove
arr= array.array('i',[7, 2, 3, 1, 5])
 
print ("The new created array is : ",end="")
for i in range (0,5):
    print (arr[i],end=" ")
print ("\n")
 
print ("The popped element is : ",end="")
print (arr.pop(2))                             #pop
 

print ("The array after popping is : ",end="")
for i in range (0,4):
    print (arr[i],end=" ")
print("\n")
 

arr.remove(7)                                 #remove
print ("The array after removing is : ",end="")
for i in range (0,3):
    print (arr[i],end=" ")


# In[20]:


#index,reverse
arr= array.array('i',[1, 2, 3, 1, 2, 5])
 
print ("The new created array is : ",end="")
for i in range (0,6):
    print (arr[i],end=" ")
print ("\n")
 

print ("The index of 1st occurrence of 3 is : ",end="")
print (arr.index(3))                                        #index

arr.reverse()                                               #reverse
print ("The array after reversing is : ",end="")
for i in range (0,6):
    print (arr[i],end=" ")

