#!/usr/bin/env python
# coding: utf-8

# # python sets

# # Set
# 
# Sets are used to store multiple items in a single variable.
# 
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# 
# A set is a collection which is both unordered and unindexed.
# 
# Sets are written with curly brackets.

# In[2]:


#creating sets
#set of strings
myset = {"apple", "banana", "cherry"}
print(myset)


# A set with strings, integers and boolean values:

# In[3]:


set1 = {"abc", 34, True, 40, "male"}


# # type

# In[4]:


print(type(myset))


# In[5]:


#Access items

for x in set1:
  print(x)


# # Python - Add Set Items

# In[6]:


set1.add("orange")

print(set1)


# # update

# In[7]:


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


# In[8]:


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


# # remove items

# In[9]:


thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


# In[10]:


#discard()

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)


# In[11]:


#pop()

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)


# In[ ]:




