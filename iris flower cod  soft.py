#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('D:\codsoft\COD/IRIS.csv')


# In[3]:


df .head()


# In[6]:


#to display stats about data


# In[7]:


df.describe()


# In[8]:


df.info()


# In[10]:


df['species'].value_counts()


# In[11]:


## Proprocessing the dataset


# In[12]:


# check the null values
df.isnull().sum()


# In[13]:


### exploratory data analysis


# In[15]:


df['sepal_length'].hist()


# In[16]:


df['sepal_width'].hist()


# In[18]:


df['petal_length'].hist()


# In[19]:


df['petal_width'].hist()


# In[20]:


## scatterplot
colors = ['red', 'orange', 'blue']
species = ['Iris-setosa','Iris-versicolor','Iris-virginica']


# In[23]:


for i in range(3):
    x = df[df['species'] == species[i]]
    plt.scatter(x['sepal_length'], x['sepal_width'], c = colors[i], label=species[i])
plt.xlabel("sepal_length")
plt.ylabel("sepal_width")
plt.legend()


# In[24]:


for i in range(3):
    x = df[df['species'] == species[i]]
    plt.scatter(x['petal_length'], x['petal_width'], c = colors[i], label=species[i])
plt.xlabel("petal_length")
plt.ylabel("petal_width")
plt.legend()


# In[25]:


for i in range(3):
    x = df[df['species'] == species[i]]
    plt.scatter(x['sepal_length'], x['petal_length'], c = colors[i], label=species[i])
plt.xlabel("sepal_length")
plt.ylabel("petal_length")
plt.legend()


# In[26]:


for i in range(3):
    x = df[df['species'] == species[i]]
    plt.scatter(x['sepal_width'], x['petal_width'], c = colors[i], label=species[i])
plt.xlabel("sepal_width")
plt.ylabel("petal_width")
plt.legend()


# In[ ]:





# In[ ]:





# In[ ]:




