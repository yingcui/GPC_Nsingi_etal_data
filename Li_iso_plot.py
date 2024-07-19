#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df = pd.read_csv('/glade/work/jnsingi/Permian-data/Li_isotope_plot.csv')
#df = df.dropna(subset='References')
df


# In[3]:


refs = list(set(df['References']))
refs


# In[4]:


mask = df["References"]==refs[0]
df[mask]


# In[5]:


clr_dict ={
    'Sun et al. (2018)': 'lime', 
    'Cao et al. (2022)': 'orangered',
}

fig, ax = plt.subplots()

for i in range(len(refs)):
    mask = df["References"]==refs[i]
    ax.scatter(df[mask]['Age (Ma)'], df[mask]['Li'], label=refs[i], color=clr_dict[refs[i]], edgecolor='k', marker='D')
ax.fill_betweenx(y=(-5, 25), x1=250.939, x2=253.000, color='magenta', alpha=0.2) # The extinction started 420 k.y before 251.939 (X1=251.939, x2=252.359) (Shen et el., 2019 - A sudden end-Permian extinction in China)
ax.set_xlim(300.0, 240.0)
ax.set_ylim(-5.0, 25.0)
ax.legend(loc='upper left', frameon=False, ncol=1, fontsize=10)
ax.set_xlabel('Time (Ma)', fontsize=14)
ax.set_ylabel(r'$\delta^{7}$Li (‰)', fontsize=14)
ax.set_xticks(np.arange(240, 301, 5)[::-1])
#ax.set_xticklabels()
ax.grid(ls=':')
#ax.set_aspect('equal')

plt.savefig('Li.pdf', bbox_inches='tight')


# In[ ]:




