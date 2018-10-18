#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


def function_for_roots(x):
    a = 1.01
    b = -3.04
    c = 2.07
    return a*x**2 + b*x + c #get the roots of ax^2 +bx + c


# In[5]:


def check_initial_valaues(f,x_min,x_max,tol):
    
    #check out initial guesses
    y_min = f(x_min)
    y_max = f(x_max)
    
    #check that c_min and c_max contain a zero crossing
    if(y_min*y_max>=0.0):
        print("No zero crossing found in the range = ",x_min,x_max)
        s = "f(%f) = %f, f(%f) = %f" % (x_min,y_min,x_max,y_max)
        print(s)
        return 0
    # if x_min is a root, then return flag == 1
    if(np.fabs(y_min)<tol):
        return 1
    
    #if x_max is a root, then return flag == 2
    if(np.fabs(y_max)<tol):
        return 2
    
    #if we reach this point, the bracket is valid
    #and we wil return 3
    return 3


# In[ ]:




