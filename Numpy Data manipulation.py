#!/usr/bin/env python
# coding: utf-8

# # Numpy
# 1.0 Numpy ndarray
# 2.0 array operations
# 3.0 staistical methords
# 4.0 Matrix class

# In[4]:


#Import Numpy
import numpy as np
data=[[2,6,1,3,7],[5,10,4,9,8]]
data=np.array(data)
print (data)


# In[8]:


#this will get us thye number of raws and columns of the array
print (data.shape)


# In[12]:


#produce an array of 0's
print (np.zeros((2,3)))


# In[13]:


#produce an array of 1's
print (np.ones((2,3)))


# In[15]:


#creating an array in the range of 30
array=np.arange(30)
print(array)


# In[16]:


# access array element from index 5 to 12
print(array[5:12])


# In[17]:


#replacing the array element from index 6 to 16 with 0
array[6:16]=0
print(array)


# # Array Operations

# In[25]:


#arithmetic Operations
data= np.array([[5,6,7],[8,9,10]])
print (data)


# In[26]:


#substaract 3 from all data elements
print(data- 3)


# In[27]:


#add 5 to all array elements
print (data +5)


# In[28]:


# squares all the array elements
print(data*data)


# In[30]:


# transposing and swapping
data=np.arange(16).reshape((4,4))
print(data)


# In[33]:


print(data.T)


# In[34]:


x=np.random.randn(2,3)
print(x)


# # statistical methords

# In[35]:


#
data= np.arange(30)
print(data)


# In[37]:


print(data.mean())


# In[39]:


print(data.max())


# In[41]:


print(data.min())


# # matrix class

# In[47]:


x=np.random.randn(2,3)
x=np.matrix(x)
y=np.random.randn(3,2)
y=np.matrix(y)
#multiply the matrices
print(x*y)


# In[ ]:





# In[ ]:




