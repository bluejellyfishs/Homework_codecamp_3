#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

# import file
df = pd.read_csv('train.csv')
df


# In[2]:


# head 10, tail 10, random 10
df.head(10)
print('-------------------------------------------------------------------------')
df.tail(10)
print('-------------------------------------------------------------------------')
df.sample(10)


# In[62]:


# delete colunm: embarked is empty
df['Embarked'].dropna()


# In[63]:


# age: empty = avg
avg = df['Age'].mean()
print(avg)
df['Age'].fillna(value=avg, inplace=True)
df.head(10)


# In[64]:


# age: empty = 0
df['Age'].fillna(value=0 ,inplace=True)
df.head(10)


# In[59]:


# delete age: empty
df.dropna(subset=['Age'],inplace=True)
df


# In[147]:


# women:men
check = df.groupby(['Sex'])
info = check.describe()
passenger = info['PassengerId']
f = passenger.loc['female','count']
m = passenger.loc['male','count']
print('Female:Male {}:{}'.format(f,m))


# In[148]:


# women & men alife
Survived = df[df['Survived'] > 0]
check = Survived.groupby(['Sex','Survived'])
info = check.describe()
passenger = info['PassengerId']
f = passenger.loc['female','count']
m = passenger.loc['male','count']
print('Female: {}'.format(f))
print('Male: {}'.format(m))


# In[149]:


# women & men alife for %
survived = df[df['Survived'] == 1]
check = survived.groupby(['Sex','Survived'])
info = check.describe()
passenger = info['PassengerId']
f = passenger.loc['female','count']
m = passenger.loc['male','count']
print('Female: {}'.format(f/314))
print('Male: {}'.format(m/577))


# In[121]:


# female = 0, male = 1
change = df['Sex'].apply(lambda x: 0 if x == 'female' else 1)
change


# In[138]:


# most age and show name age embarked
df.describe()
df[df['Age'] == 80][['Name', 'Age', 'Embarked']]


# In[134]:


# less age and show name age embarked
df.describe()
df[df['Age'] == 0.42][['Name', 'Age', 'Embarked']]


# In[144]:


# the most expentive price show name age embarked
info = df.describe()
df[df['Fare'] == info.loc['max','Fare']][['Name', 'Age', 'Embarked']]


# In[143]:


# the less expentive price show name age embarked
info = df.describe()
df[df['Fare'] == info.loc['min','Fare']][['Name', 'Age', 'Embarked']]


# In[155]:


# How much 1 2 3 Pclass
check = df.groupby('Pclass')
info = check.describe()
passenger = info['PassengerId']
passenger['count']


# In[160]:


# mean 1 2 3 Pclass
check = df.groupby('Pclass')
info = check.describe()
info['PassengerId']
passenger['mean']


# In[167]:


# count age > 50 and survived
age = df[df['Age'] > 50]
age[age['Survived'] == 1].count().loc['Survived']


# In[172]:


# show info 1 2 3 PClass
check = df.groupby('Pclass')
check.describe()


# In[174]:


# show info Fare
check = df.groupby('Pclass')
info = check.describe()
info['Fare']


# In[200]:


# 0-10, 11-20, +10 each survived rate1:rate2:rate3:...
survived = df[df['Survived'] == 1]
rate_0_10 = survived[survived['Age'] <= 10]
rate_0_10.describe()
sur_c_1 = info['Survived']
rate_1 = sur_c_1['count']

rate_11_20 = survived[(survived['Age'] > 10) & (survived['Age'] <= 20)]
info = rate_11_20.describe()
sur_c_2 = info['Survived']
rate_2 = sur_c_2['count']

rate_21_30 = survived[(survived['Age'] > 20) & (survived['Age'] <= 30)]
info = rate_21_30.describe()
sur_c_3 = info['Survived']
rate_3 = sur_c_3['count']

rate_31_40 = survived[(survived['Age'] > 30) & (survived['Age'] <= 40)]
info = rate_31_40.describe()
sur_c_4 = info['Survived']
rate_4 = sur_c_4['count']

rate_41_50 = survived[(survived['Age'] > 40) & (survived['Age'] <= 50)]
info = rate_41_50.describe()
sur_c_5 = info['Survived']
rate_5 = sur_c_5['count']

rate_51_60 = survived[(survived['Age'] > 50) & (survived['Age'] <= 60)]
info = rate_51_60.describe()
sur_c_6 = info['Survived']
rate_6 = sur_c_6['count']

rate_61_70 = survived[(survived['Age'] > 60) & (survived['Age'] <= 70)]
info = rate_61_70.describe()
sur_c_7 = info['Survived']
rate_7 = sur_c_7['count']

rate_71_80 = survived[(survived['Age'] > 10) & (survived['Age'] <= 80)]
info = rate_71_80.describe()
sur_c_8 = info['Survived']
rate_8 = sur_c_8['count']

print('rate {}:{}:{}:{}:{}:{}:{}:{}'.format(rate_1, rate_2, rate_3, rate_4, rate_5, rate_6, rate_7, rate_8))


# In[202]:


# sort fare: high to low, low to high
asc = df.sort_values(by=['Fare'])

desc = df.sort_values(by=['Fare'])[::-1]


# In[239]:


# lastname no duplicate and count preple
df['Last'] = df.apply(lambda row: row.Name.split(',')[0], axis = 1)
df[df.duplicated('Last', keep=False)].count()


# In[22]:


# lastname duplicate and count lastname
df['Last'] = df.apply(lambda row: row.Name.split(',')[0], axis = 1)
l = df['Last'].value_counts()
l[l > 1].index


# In[ ]:




