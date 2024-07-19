#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df = pd.read_csv('/glade/work/jnsingi/Permian-data/Sr_isotope_plot.csv', encoding="ISO-8859-1")


# In[3]:


df = df.dropna(subset='Reference')
df


# In[4]:


refs = list(set(df['Reference']))
refs


# In[5]:


mask = df["Reference"]==refs[0]
df[mask]


# In[11]:


clr_dict ={
    'Veizer and Compston (1974)': 'blue',
    'Song et al. (2015)' : 'yellow',
    'Cao et al. (2022)' : 'lime',
    'Sedlacek et al. (2014)' : 'crimson',
    'Korte et al. (2003)' : 'deepskyblue',
    'Morante (1996)' : 'cyan',
    'Korte et al. (2006)' : 'magenta',
    'Marting and Madcougall (1995)' : 'darkorange',
    'Wang et al. (2021)' : 'dodgerblue',
}

fig, ax = plt.subplots()

for i in range(len(refs)):
    mask = df["Reference"]==refs[i]
    ax.scatter(df[mask]['Age (Ma)'], df[mask]['Sr'], label=refs[i], color=clr_dict[refs[i]], edgecolor='k', marker='D')
ax.fill_betweenx(y=(0.7060, 0.7110), x1=251.000, x2=253.000, color='magenta', alpha=0.3) # The extinction started 420 k.y before 251.939 (Shen et el., 2019 - A sudden end-Permian extinction in China)
ax.set_xlim(300.0, 230.0) 
ax.set_ylim(0.7060, 0.7110)
ax.legend(frameon=False, ncol=1, fontsize=8.5)
ax.set_xlabel('Time (Ma)', fontsize=12)
ax.set_ylabel(r'$^{87/86}$Sr', fontsize=12)
ax.set_xticks(np.arange(230, 301, 5)[::-1])
ax.grid(ls=':')

#plt.savefig('Sr.pdf', bbox_inches='tight')


# In[ ]:




