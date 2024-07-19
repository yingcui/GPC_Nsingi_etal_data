#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import numpy as np


# In[38]:


df = pd.read_csv('/glade/work/jnsingi/Permian-data/Osmium_data_Age.csv')
df


# In[39]:


refs = list(set(df['References']))
refs


# In[41]:


mask = df["References"]==refs[0]
df[mask]


# In[43]:


clr_dict ={
    'Georgiev et al. (2020)':'yellow',
    'Liu et al. (2019)': 'cyan',
    'Liu et al. (2020)': 'magenta',
    'Liu and Selby (2021)': 'darkorange',
}

fig, ax = plt.subplots()

for i in range(len(refs)):
    mask = df["References"]==refs[i]
    ax.scatter(df[mask]['Age (Ma)'], df[mask]['Osi'], label=refs[i], color=clr_dict[refs[i]], edgecolor='k', marker='D')
ax.fill_betweenx(y=(0.0, 2.0), x1=251.939, x2=252.359, color='red', alpha=0.3) # The extinction started 420 k.y before 251.939 (Shen et el., 2019 - A sudden end-Permian extinction in China)
ax.set_xlim(256.0, 250.0)
ax.set_ylim(0.00, 1.75)
ax.legend(loc='upper left', frameon=False, ncol=1, fontsize=9)
ax.set_xlabel('Time (Ma)', fontsize=14)
ax.set_ylabel(r'$Os_{i}$', fontsize=14)
ax.grid(ls=':')

#Annotation

ax.text(255.25, 0.04, 'Magmatism', fontsize=8) #Magmatism1
ax.text(251.77, 0.04, 'Magmatism', fontsize=8) #Magmatism2
ax.text(251.5, 1.46, 'Enhanced weathering', fontsize=8) #Enhanced weathering

#Arrows

opt = dict(color='blue', width=6)

a1=gca().annotate('', xy=(254.31, 0.14), xytext=(254.31, 0.0), arrowprops=opt) #Magmatism1
a2=gca().annotate('', xy=(251.90, 0.15), xytext=(251.91, 0.0), arrowprops=opt) #Magmatism2
a3=gca().annotate('', xy=(251.62, 1.28), xytext=(251.63, 1.75), arrowprops=opt) #Enhanced weathering

#plt.savefig('Os-_Age.pdf', bbox_inches='tight')


# In[45]:


clr_dict ={
    'Georgiev et al. (2020)':'yellow',
    'Liu et al. (2019)': 'cyan',
    'Liu et al. (2020)': 'magenta',
    'Liu and Selby (2021)': 'darkorange',
}

fig, ax = plt.subplots()

for i in range(len(refs)):
    mask = df["References"]==refs[i]
    ax.scatter(df[mask]['Age (Ma)'], df[mask]['Osi'], label=refs[i], color=clr_dict[refs[i]], edgecolor='k', marker='D')
ax.fill_betweenx(y=(0.0, 2.0), x1=251.939, x2=252.359, color='red', alpha=0.3) # The extinction started 420 k.y before 251.939 (Shen et el., 2019 - A sudden end-Permian extinction in China)
ax.set_xlim(256.0, 250.0)
ax.set_ylim(0.00, 1.60)
ax.legend(loc='upper left', frameon=False, ncol=1, fontsize=9)
ax.set_xlabel('Time (Ma)', fontsize=14)
ax.set_ylabel(r'$Os_{i}$', fontsize=14)
ax.grid(ls=':')

#Annotation

ax.text(255.25, 0.04, 'Magmatism', fontsize=8) #Magmatism1
ax.text(251.77, 0.04, 'Magmatism', fontsize=8) #Magmatism2
ax.text(251.5, 1.46, 'Enhanced weathering', fontsize=8) #Enhanced weathering

#Arrows

opt = dict(color='blue', width=6)

a1=gca().annotate('', xy=(254.31, 0.14), xytext=(254.31, 0.0), arrowprops=opt) #Magmatism1
a2=gca().annotate('', xy=(251.90, 0.15), xytext=(251.91, 0.0), arrowprops=opt) #Magmatism2
a3=gca().annotate('', xy=(251.62, 1.28), xytext=(251.63, 1.60), arrowprops=opt) #Enhanced weathering

#plt.savefig('Osi_Age.pdf', bbox_inches='tight')


# In[ ]:




