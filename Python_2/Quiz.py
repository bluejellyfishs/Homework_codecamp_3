#!/usr/bin/env python
# coding: utf-8

# In[4]:


a = input()

if(int(a) == 0):
    print("เลขศูนย์")
elif(int(a)%2 == 0):
    print("เลขคู่")
elif(int(a)%2 != 0):
    print("เลขคี่")    


# In[6]:


a = float(input())
b = float(input())

while b == 0:
    b = float(input())
    
print(a/b)


# In[7]:


a = int(input())
count = 1
total = a

while a != 0:
    a = int(input())
    total += a 
    count += 1
else: 
    print(total/count)


# In[9]:


a = int(input())

if (a%7 != 0):
    print("หาร 7 ไม่ลงตัว")
else:
    print("หาร 7 ลงตัว")    


# In[10]:


a = int(input())
b = int(input())
c = int(input())

if (a**2 == (b**2 + c**2)) | (b**2 == (a**2 + c**2)) | (c**2 == (b**2 + a**2)):
    print("True")
else:
    print("False")


# In[12]:


a = int(input())
b = int(input())
c = int(input())

if (a**2 == (b**2 + c**2)) | (b**2 == (a**2 + c**2)) | (c**2 == (b**2 + a**2)):
    print("สามเหลี่ยมมุมฉาก")
elif (a**2 > (b**2 + c**2)) | (b**2 > (a**2 + c**2)) | (c**2 > (b**2 + a**2)):
    print("สามเหลี่ยมมุมป้าน")  
else:
    print("สามเหลี่ยมมุมแหลม")


# In[13]:


a = int(input())
b = int(input())
c = int(input())
while (a < 1000) | (a > 5000) | (b < 1000) | (b > 5000) | (c < 1000) | (c > 5000):
    if (a < 1000) | (a > 5000):
       a = int(input("กรุณากรอกข้อมูลที่ 1 ใหม่:")) 
    if (b < 1000) | (b > 5000):
       b = int(input("กรุณากรอกข้อมูลที่ 2 ใหม่:")) 
    if (c < 1000) | (c > 5000):
       c = int(input("กรุณากรอกข้อมูลที่ 3 ใหม่:")) 
else:
    total = a + b + c
    if (total > 12000):
        total *= 0.75
    elif (total > 6000):
        total *= 0.85
    print(total)    


# In[14]:


a = int(input())
b = int(input())
c = int(input())
d = int(input())

while (a < 1000) | (a > 5000) | (b < 1000) | (b > 5000) | (c < 1000) | (c > 5000) | (d < 1000) | (d > 5000):
    if (a < 1000) | (a > 5000):
       a = int(input("กรุณากรอกข้อมูลที่ 1 ใหม่:")) 
    if (b < 1000) | (b > 5000):
       b = int(input("กรุณากรอกข้อมูลที่ 2 ใหม่:")) 
    if (c < 1000) | (c > 5000):
       c = int(input("กรุณากรอกข้อมูลที่ 3 ใหม่:")) 
    if (d < 1000) | (d > 5000):
       d = int(input("กรุณากรอกข้อมูลที่ 4 ใหม่:"))    
else:
    total = a + b + c
    if (total > 12000):
        d *= 0.75
    elif (total > 6000):
        d *= 0.85
    print(d)   


# In[15]:


a = int(input())
b = int(input())
c = int(input())
d = int(input())

while (a < 1000) | (a > 5000) | (b < 1000) | (b > 5000) | (c < 1000) | (c > 5000) | (d < 1000) | (d > 5000):
    if (a < 1000) | (a > 5000):
       a = int(input("กรุณากรอกข้อมูลที่ 1 ใหม่:")) 
    if (b < 1000) | (b > 5000):
       b = int(input("กรุณากรอกข้อมูลที่ 2 ใหม่:")) 
    if (c < 1000) | (c > 5000):
       c = int(input("กรุณากรอกข้อมูลที่ 3 ใหม่:")) 
    if (d < 1000) | (d > 5000):
       d = int(input("กรุณากรอกข้อมูลที่ 4 ใหม่:"))    
else:
    total = a + b + c
    if (total > 9000):
        d *= 0.70
    elif (total > 4000):
        d *= 0.75
    print(d)  


# In[ ]:


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = bool(input("Cedit?"))

while (a < 1000) | (a > 5000) | (b < 1000) | (b > 5000) | (c < 1000) | (c > 5000) | (d < 1000) | (d > 5000):
    if (a < 1000) | (a > 5000):
       a = int(input("กรุณากรอกข้อมูลที่ 1 ใหม่:")) 
    if (b < 1000) | (b > 5000):
       b = int(input("กรุณากรอกข้อมูลที่ 2 ใหม่:")) 
    if (c < 1000) | (c > 5000):
       c = int(input("กรุณากรอกข้อมูลที่ 3 ใหม่:")) 
    if (d < 1000) | (d > 5000):
       d = int(input("กรุณากรอกข้อมูลที่ 4 ใหม่:"))    
else:
    total = a + b + c
    if (total > 9000):
        d *= 0.70
    elif (total > 4000):
        d *= 0.75
    if (e == True):
        d *= 0.95   
    print(d) 


# In[ ]:


a = input("character >= 7: ")
b = ""
for i in a:
    if (i.isupper()):        
        b += i.lower()
    else:
        b += i.upper()
    
print(b) 


# In[ ]:


a = input()
b = input()
c = input()
d = input()

e = len(a)
f = len(b)
g = len(c)
h = len(d)

dic = {a: e, b: f, c: g, d: h}
{k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}
for key, value in dic.items():
    print(key)


# In[ ]:


a = int(input("0 - 60: "))
b = int(input("0 - 60: "))

print(a*150 + b*2)


# In[ ]:


a = int(input("0 - 60: "))
b = int(input("0 - 60: "))

if (a == 0):
    print("Free")
else:
    if (b > 15):
        print((a-1)*300 + 300)
    else:    
        print((a-1)*300)


# In[ ]:


a = int(input())
b = int(input())

x = (-b/2)+2*a
y = a-x

print(x*150 + y*220)


# In[ ]:





# In[ ]:




