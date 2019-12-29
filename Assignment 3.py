#!/usr/bin/env python
# coding: utf-8

# Write a function to compute 5/0 and use try/except to catch the exceptions.

# In[25]:


def division():
    return 5/0
try:
    division()
except Exception as e:
    print(e)


# Implement a Python program to generate all sentences where subject is in ["Americans",
# "Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"].
# Hint: Subject,Verb and Object should be declared in the program as shown below.
# subjects=["Americans ","Indians"]
# verbs=["play","watch"]
# objects=["Baseball","Cricket"]
# Output should come as below:
# Americans play Baseball.
# Americans play Cricket.
# Americans watch Baseball.
# Americans watch Cricket.
# Indians play Baseball.
# Indians play Cricket.
# Indians watch Baseball.
# Indians watch Cricket.

# In[24]:


subjects=["Americans", "Indians"]
verbs=["Play", "watch"]
objects=["Baseball","cricket"]

all_sentences = [(i+" "+ j + " " + k) for i in subjects for j in verbs for k in objects]
for x in all_sentences:
 print (x)


# Write a function so that the columns of the output matrix are powers of the input vector.
# The order of the powers is determined by the increasing boolean argument. Specifically, when
# increasing is False, the i-th output column is the input vector raised element-wise to the power
# of N - i - 1.
# HINT: Such a matrix with a geometric progression in each row is named for AlexandreTheophile Vandermonde

# In[47]:




