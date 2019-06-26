#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.listdir()


# In[2]:


import pandas


# In[5]:


pandas.show_versions()


# In[9]:


df2 = pandas.read_json("supermarkets.json")
df2


# In[13]:


dir(pandas)


# In[22]:


df5 = pandas.read_excel("supermarkets.xlsx")
df5


# In[23]:


df10 = pandas.read_csv("supermarkets_semi-colons.txt")
df10


# In[24]:


df11 = pandas.read_csv("supermarkets_commas.txt")
df11


# In[27]:


df13 = pandas.read_csv("supermarkets.csv")
df13


# In[28]:


df13.set_index("Address")


# In[29]:


df13


# In[ ]:




