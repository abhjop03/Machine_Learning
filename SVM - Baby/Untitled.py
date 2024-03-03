#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles


# In[13]:


data, labels = make_circles(n_samples = 1000, noise = 0.1, factor = 0.2)


# In[14]:


plt.scatter(data[:, 0], data[:, 1], c = labels)


# In[15]:


print(data.shape)


# In[19]:


x = data[:, 0].reshape(-1, 1)
y = data[:, 1].reshape(-1, 1)
axis_3 = x**2 + y**2


# In[20]:


dataset = np.hstack((data, axis_3))


# In[21]:


dataset.shape


# In[25]:


ax = plt.subplot(projection = '3d')
ax.scatter(x, y, axis_3, c = labels)
plt.show()


# In[ ]:




