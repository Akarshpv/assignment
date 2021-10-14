#!/usr/bin/env python
# coding: utf-8

# In[26]:


my_tuple = (i for i in range(1,21))
a_list = list(my_tuple)
for i in range(0,20):
    if i%2!=0:
        a_list[i]='e'
a_tuple = tuple(a_list)
print(a_tuple)
print(type(a_tuple))


# In[ ]:




