#!/usr/bin/env python
# coding: utf-8

# In[1]:


import array as arr

x = arr.array('i',[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(x)

y = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print(y)


# In[5]:


import array as arr

x = arr.array('i',[1, 1, 1, 1, 1])
print(x)

y = [[1, 1, 1], [1, 1, 1], [1, 1, 1]] 
print(y)


# In[4]:


import numpy as np
import time

t3 = time.time()

x = np.random.uniform(10, 100, 20)
print(x*2)
t4 = time.time()

n = t4-t3


# In[35]:


import random

t1 = time.time()

y = []
for i in range(20):
    x = random.uniform(10, 100)
    y.append(x*2)
print(y)

t2 = time.time()
l = t2-t1


# In[36]:


print(l-n)


# In[38]:


x = np.arange(10, 1001)

print(x)


# In[39]:


x = np.arange(10, 2001, 2)

print(x)


# In[45]:


x = np.arange(13, 900, 2)

print(x)


# In[46]:


x = np.identity(4)
print(x)


# In[48]:


x = np.random.randint(5, 25, 100)
print(np.std(x))


# In[49]:


x = np.random.uniform(0, 1, 1)
print(x)


# In[53]:


x = np.random.randint(50, 101, (4,4))
print(x)
print(x.T)


# In[85]:


x = np.arange(1, 26)
y = np.array(x.reshape(5,5))
print(y)
print(y[1:3,2:4])


# In[90]:


print(y[3,2:])


# In[91]:


print(y[3:6,:2])


# In[92]:


print(y[2])


# In[96]:


x = np.random.randint(10, 100, (5,5))
print(x[x > 50])
print(x[x > 40])


# In[7]:


x = np.random.randint(10, 100, (3,3))
t = x.T
print(t[2][2])


# In[ ]:




