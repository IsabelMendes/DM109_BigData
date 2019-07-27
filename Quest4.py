#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_json('telemetry.json', lines=True)
df.head()


# In[5]:


car4 =  json_normalize( df[df['Car']==4]['telemetry'] )
car4.head()


# In[8]:


# Velocidade do carro 4
car4['Speed'] = car4['Speed'] * (35/9)
car4['Speed'].plot(kind='line', grid=True, y=['Speed'], color="blue")
plt.xlabel('Time (s)')
plt.ylabel('Speed (Km/h)')


# In[48]:


# Carro5
car5 =  json_normalize( df[df['Car']==5]['telemetry'] )
car5.head()


# In[49]:


#Velocidade do carro 5
car5['Speed'] = car5['Speed'] * (35/9)
car5['Speed'].plot(kind='line', grid=True, y=['Speed'], color="red")
plt.xlabel('Time (s)')
plt.ylabel('Speed (Km/h)')


# In[50]:


#Comparando as velocidades dos carros 4 e 5
plt.plot(car4['Speed'], color='blue')
plt.plot(car5['Speed'], color='red')
plt.xlabel('Time (s)')
plt.ylabel('Speed (Km/h)')


# In[51]:


# RPM do carro 4
rpm = car4['RPM']
rpm.plot(kind='line', y=['RPM'], grid=True, color='red')
plt.xlabel('Time (s)')
plt.ylabel('RPM')


# In[52]:


# Gear do carro 4
gear = car4['Gear']
gear.plot(kind='line', y=['Gear'], grid=True, color='green')
plt.xlabel('Time (s)')
plt.ylabel('Gear')


# In[53]:


fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('RPM', color=color)
ax1.plot(rpm, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()  # instantiate a second axes
color = 'tab:green'
ax2.set_ylabel('Gear', color=color)
ax2.plot(gear, color=color, linewidth=2)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()
plt.show()


# In[54]:


# Gasto de combustível do carro 5
gas = car5['Fuel']
car5['Fuel'].plot(kind='line', grid=True, y=['Fuel'], color="pink")


# In[64]:


# Gasto de combustível do carro 4
gas = car4['Fuel']
car4['Fuel'].plot(kind='line', grid=True, y=['Fuel'], color="black")


# In[62]:


#Comparando o gasto de combustível dos carros 4 e 5
#Podemos observar que o gasto foi praticamente igual nos primeiros 700 s da corrida. Depois disso, o carro 5 gastou mais que o carro 4.
plt.plot(car4['Fuel'], color='black')
plt.plot(car5['Fuel'], color='pink')
plt.xlabel('Time (s)')
plt.ylabel('Gas')


# In[ ]:




