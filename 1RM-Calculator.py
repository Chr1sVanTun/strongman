
# coding: utf-8

# # Calculating the 1 Rep Maximum (1RM) for your strength disciplines

# Upper Body Exercises
# 
# Find the heaviest weight you can lift 4-6 times and plug it into this equation: (kg * 1.1307) + 0.6998.
# 
# So if you can do 5 reps of 60kg, then according to the formula – 
# (60 *1.1307) + 0.6998 – your 1RM will be 68.5kg. 
# 
# For lower body use this formula: (4-6RM x 1.09703) + 14.2546.

# # Upper Body

# In[1]:


kgU = float(input())

RMU = (kgU * 1.1307) + 0.6998

"Your 1RM is approximately: " + str(RMU) + " kg"


# # Lower Body

# In[3]:


kgL = float(input())

RML = (kgL * 1.09703) + 14.2546

"Your 1RM is approximately: " + str(RML) + " kg"

