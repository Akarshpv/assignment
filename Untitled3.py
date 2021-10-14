#!/usr/bin/env python
# coding: utf-8

# In[10]:


my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
my_list = list(my_tuple)

# print original
print("Original:")
print (my_tuple)

# loop to traverse each element in the list
# and, remove elements
# which are EVEN (divisible by 2)
for i  in my_list:
	if(i%2 == 0):
	    my_list[i =='e']

# print list after removing EVEN elements
print ("list after removing EVEN numbers:")
print (my_list)


# In[26]:


x = "seMi Long StRing WiTH COMPLetely RaNDOM CasINg"
result_string = ""
index = 0;
for c in x:
    if(index%2 == 0):
        result_string += c.replace('s','0')
    else:
        result_string += c.upper()
    index+=1

print(result_string)


# In[35]:


months = ('Jan','Feb','Mar','April','May','June','July','Aug','Spet','Oct','Nov','Dec')
days = ('Sun','Mon','Tue','Wed','Thur',)
year = months + days
print(year)


# In[33]:





# In[1]:





# In[ ]:




