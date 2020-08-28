#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


x = np.arange(0, 11)
y = x**2
plt.title('Exponential Line Graph')
plt.xlabel('Number 1-10')
plt.ylabel('X ** 2')
plt.plot(x, y)


# In[8]:


x = np.arange(0, 90)
y = np.sin(x)
plt.title('Sin Graph')
plt.xlabel('Number 1-90')
plt.ylabel('sin(x)')
plt.plot(x, y, c ='pink')


# In[9]:


y = np.arange(0, 10)
x = y**2
plt.title('Exponential Line Graph')
plt.ylabel('Number 1-9')
plt.xlabel('Y ** 2')
plt.plot(x, y, c ='#7CFC00')


# In[11]:


x = np.arange(0, 20)
y = np.cos(x)
plt.title('Cos Graph')
plt.xlabel('Number 1-90')
plt.ylabel('sin(x)')
plt.plot(x, y, c ='red', ls='--')


# In[15]:


x = np.arange(0, 10)
y1 = x**2
y2 = x**3
plt.title('Exponential Line Graph')
plt.xlabel('Number 1-9')
plt.ylabel('Exponential')
plt.plot(x, y1, c='red', marker='o')
plt.plot(x, y2, c='blue', marker='v')


# In[18]:


y = np.arange(0, 10)
x1 = y**2
x2 = y**3
plt.title('Exponential Line Graph')
plt.ylabel('Number 1-9')
plt.xlabel('Exponential')
plt.plot(y, x1, c='red', marker='o', label='y**2')
plt.plot(y, x2, c='blue', marker='v', label='y**3')
plt.grid()
plt.legend()


# In[23]:


y = np.arange(0, 100)
x = y**2 + 4*y
plt.title('Calculate Line Graph')
plt.ylabel('Number 1-99')
plt.xlabel('y**2 + 4*y')
plt.plot(x, y, c='#FFD700')
plt.xlim([1000, 10000])
plt.ylim([10, 100])


# In[31]:


x = np.arange(0, 30)
y = np.cos(x)
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1, 0.95, 0.85])
ax1.plot(y**3, y, label='x = y**3')
ax2 = fig.add_axes([0.7, 0.2, 0.3, 0.3])
ax2.plot(y*3, x**2 + 2, label='x = y*3')
plt.title('Graph')
plt.ylabel('Number 1-29')
plt.xlabel('Exponential')
plt.legend()


# In[9]:


import pandas as pd
df = pd.read_csv('train.csv')
df


# In[47]:


check = df.groupby('Pclass')
info = check.describe()
passenger = info['PassengerId']
passenger['count']
y = [216, 184, 491]
plt.pie(y, labels=['Class1', 'Class2', 'Class3'])


# In[56]:


check = df.groupby('Embarked')
info = check.describe()
passenger = info['PassengerId']

explode = [0, 0.1, 0]
plt.pie([passenger['count']], labels=['Cherbourg', 'Queenstown', 'Southampton'], explode=explode)


# In[58]:


df['Fare']
plt.hist(df['Fare'])


# In[60]:


x = df['Age']
y = df['Fare']
plt.scatter(x, y)


# In[66]:


check = df.groupby('Pclass')
info = check.describe()
fare = info['Fare']
y = fare['mean']
plt.bar([1, 2, 3], y)


# In[16]:


check = df.groupby('Age')
check.describe()
info = check.describe()
fare = info['Fare']
y = fare['mean']
x = info.index
plt.bar(x, y)


# In[18]:


df['Last'] = df.apply(lambda row: row.Name.split(',')[0], axis = 1)
l = df['Last'].value_counts()
y = l[l > 1]
plt.bar(y.index, y)


# In[20]:


check = df.groupby('Pclass')
info = check.describe()
fare = info['Fare']
y = fare['mean']

checkE = df.groupby('Embarked')
infoE = checkE.describe()
passenger = infoE['PassengerId']
explode = [0, 0.1, 0]

plt.figure(figsize = [10, 15])
plt.subplot(3, 2, 1)
plt.bar([1, 2, 3], y)
plt.title('Fare Mean')
plt.ylabel('Dollrs')
plt.xlabel('PClass')

plt.subplot(3, 2, 3)
plt.scatter(df['Age'], df['Fare'])
plt.title('Age:Fare')
plt.ylabel('Fare')
plt.xlabel('Age')

plt.subplot(3, 2, 5)
plt.pie([passenger['count']], labels=['Cherbourg', 'Queenstown', 'Southampton'], explode=explode)
plt.title('Embarked')

plt.subplot(2, 2, 2)
plt.hist(df['Fare'])
plt.title('Fare')
plt.ylabel('count')
plt.xlabel('Fare')

check = df.groupby('Age')
check.describe()
info = check.describe()
fare = info['Fare']
y = fare['mean']
x = info.index

plt.subplot(2, 2, 4)
plt.bar(x, y)
plt.title('Survived:Sex')
plt.xlabel('Fare')


# In[ ]:




