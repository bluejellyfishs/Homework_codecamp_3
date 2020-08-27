#!/usr/bin/env python
# coding: utf-8

# In[1]:


2345%13


# In[2]:


1567//17


# In[4]:


# ไม่ เพราะเป็น case sensitive


# In[ ]:


# ไม่ เพราะ ตัวอักษรควรขึ้นก่อนตัวเลข และมีเครื่องหมาย '_' คั่น


# In[5]:


print('2345%13 = {}'.format(2345%13))


# In[6]:


print('1567//17 = {}'.format(1567//17))


# In[ ]:


div = lambda x: x/3
print(div(9))


# In[ ]:


def avg(a, b, c, d):
    return (a+b+c+d)/4
print(avg(2, 4, 6, 8))


# In[ ]:


avg = lambda a, b, c, d: (a+b+c+d)/4
print(avg(2, 4, 6, 10))


# In[ ]:


lst = ["Waranya", "Thamsritip", 25]


# In[ ]:


lst.remove(25)
print(lst)


# In[ ]:


lst.insert(0, 15)
print(lst)


# In[ ]:


lst.append(150)
lst.append(40)
print(lst)


# In[ ]:


print(lst[2:])


# In[ ]:


a = [[[1, 3], [3, 4]], [5, [5, 6], [7, 8]]]
print(a[1][1][1])


# In[ ]:


lst = [["Waranya", "Thamsritip", 25],
      ["Natchanon", "Thamsritip", 22],
      ["Napichaya", "Thamsritip", 27],
      ["Vichit", "Thamsritip", 55]]
print(lst)


# In[ ]:


lst.remove(["Vichit", "Thamsritip", 55])
print(lst)


# In[ ]:


lst.insert(0,["Suranich", "Tungjitmansakil", 54])
print(lst)


# In[ ]:


lst[1][2] = 44
print(lst)


# In[ ]:


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[ ]:


lamb_m =  map(lambda x: x**3, lst)
print(list(lamb_m))


# In[ ]:


def power_f(a):
    return a**3

print(list(map(power_f, lst)))


# In[ ]:


lamb_f =  filter(lambda x: (x**2)%2 == 1, lst)
print(list(lamb_f))


# In[ ]:


def mod_f(a):
    return (a**2)%2 == 1

print(list(filter(mod_f, lst)))


# In[ ]:


lst = [1, 2, 3, 4, 5]
mul = [i*2-1 for i in lst]
print(mul)


# In[ ]:


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
div = [i**3 for i in lst if i%3 != 0]
print(div)


# In[ ]:


A = [1, 2, 3, 4, 5]
B = [2, 3, 1, 2, 3]

def func(x, y):
    return y**x
power_f = map(func, A, B)
print(list(power_f))


# In[ ]:


name_lst = ["Ant", "Anny", "Anna"]
no_lst = ["1", "2", "3"]
score_lst = [80, 75, 83]

mapped = list(zip(name_lst, no_lst, score_lst))
print(mapped)


# In[ ]:


from functools import reduce

lst = [5, 2, 1, 3, 2]

a = reduce(lambda x, y: x**y, lst)
print(a)


# In[ ]:


from functools import reduce

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = reduce(lambda x, y: x*y, lst)
print(a)

