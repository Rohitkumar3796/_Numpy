#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
i=np.array(10)
print(i)
print(i.ndim,"dimension")


# In[6]:


a=np.array([1,2,3])
print(a)


# In[22]:


b=np.array([[1,2,3,4,5],
            [5,6,7,8,9],
            [1,5,4,2,6]])
print(b)


# In[18]:


c=np.array([[[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12]],
           [[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12]]])
          

print(c)


# In[23]:


#Get Dimension
print(a.ndim)
print(b.ndim)
print(c.ndim)


# In[65]:


#Get Shape
# Shape returns number of elements in each
# dimension
# It returns a tuple with each index.
print(a.shape) #here 3 means column
print(b.shape) #2 & 5 means two rows and 5 columns
print(c.shape)# 2 means two arrays in 3 dimesional array & 3 means rows and 4 means column#


# In[25]:


#slicing
print(a[2])
print(a[1:3])
print(b[1][2])
print(b[0][0:2])
print(c[0][2][1])
print(c[1][1][1])
print(c[0][0][2:])


# In[27]:


#slicing with steps
print(a[1::2])
print(b[1][0::2])
print(c[0][1][0::2])


# In[28]:


#array and element slicing
print(b[0:2,0:2])# here we did slicing arrays with its element


# In[29]:


#negative Indexing
print(b[1][-4:])


# In[33]:


#we can also give size to array
print(a,np.int32)
print(b,np.int64)
print(c,np.int64)
# here we can check type and size of the array
print(a.dtype)
print(b.dtype)
print(c.dtype)


# In[55]:


#dtype tells the type of data
#astype converts the given data into what type do you want
# we have a int type array so we converts its into string
e=np.array([100,200,300,400,500])
s=e.astype('S')
print(s.dtype)
# here we use astype to convert int to float
print(e.dtype)
fl=e.astype('f')
print(fl.dtype)
# here we convert int into bool 
print(e.dtype)
t_f=e.astype('bool')
print(t_f.dtype)


# In[60]:


i=np.array([70,60,30,40,50])
# copy() function behaves like if you make a copy of given data, and make changes in copy of data
# so it is not affected on original data(You make a just temporary file)
j=i.copy()
print(i)
i[0]=10 #here i change the value of i 
i[1]=20
print(i) #here u can see the value of i is changed but the value of j is not changed
print(j)


# In[62]:


j=np.array([1,2,3,4,5])
k=j.view()
print(j)
# if i change the data of j so it will affect on k's data
j[0]=8
print(j)
print(k)
#here you can  see the jth and kth data 


# In[102]:


# From reshape() function we can print the value in the one dimensional array
# we can convert 2 dimesional to one dimensional
z=np.array([[1,2,3,],
           [4,5,6],
           [7,8,9]])
print(z)
x=z.reshape(-1) #or i can give here also how much element in the array like 9
print(x)
a=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# here i have reshaped the one dimesional to 2 dimesional array
reshape_a=a.reshape(3,3)
print(reshape_a)


# In[76]:


# Access Element by For loop
z=np.array([[1,2,3,],
           [4,5,6],
           [7,8,9]])
for i in z:
    for j in i:
        print(j)
    


# In[87]:


# From random in numpy we can take randomly values to array
from numpy import random
i=random.rand()
print(i)
# here i can take 11 float value
j = random.rand(11)
print(j)
k=random.randint(100,size=(10)) #one dimensional because of i have given here only 10 the size of elements
print(k,'one dimesional')
l=random.randint(100, size=(3,5)) # here it is 2 dimensional because of 3 is row and 5 is column
print(l,'two dimesional')
m=random.randint(100, size=(3,3,2)) #fisrt 3 means 3 arrays and another 3 is for row and 2 is for column
print(m,'three dimensional')


# In[92]:


#we have given a list and use choice function to choose the element from list and make a 2 dimensional array
from numpy import random
list1=[10,20,30,40,50,60,70,80,90,100]
i=random.choice(list1,size=(4,3)) #4 means row and 3 mean columns
print(i)


# In[94]:


# here i can also multiply the elements but we cannot do this with list
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(arr1*arr2)


# In[100]:


#here we can concatenate the arrays in one array with concatenate function
# one dimensional
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.concatenate((arr1,arr2))
print(arr,':One dimensional')
# two dimensional
arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[10,20,30],[40,50,60]])
arr=np.concatenate((arr1,arr2))
print(arr,':Two dimensional')


# In[111]:


#here i used stack function to print arrays in rows or column using 0 and 1 value
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr=np.stack((arr1,arr2), axis=0) #0 row and 1 culumn
print(arr) #row
arr=np.stack((arr1,arr2), axis=1)
print(arr) #column


# In[113]:


#here i used array_split() function to split array element to different arrays
arr = np.array([1, 2, 3, 4, 5, 6])
newarr=np.array_split(arr,4)
print(newarr)


# In[114]:


#here i search the element in the array by where function
arr=np.array([1,2,3,4,5])
ans=np.where(arr==2)
print(ans)


# In[115]:


#here i use sort function to sort the element in the array
arr=np.array([4,1,3,2])
arr.sort()
print(arr)

