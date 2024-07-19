#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df = pd.read_csv('/glade/work/jnsingi/Permian-data/Ca_isotope_plot.csv')
#df = df.dropna(subset='Section')
df


# In[3]:


secs = list(set(df['Section']))
secs


# In[4]:


clr_dict = {
    'Saiq Plateau section': 'lime',
    'Tesero Road section': 'fuchsia',
    'Dajiang section': 'darkorange',
    'Taskent section': 'aqua',
}

fig, ax = plt.subplots()

for i in range(len(secs)):
    mask = df["Section"]==secs[i]
    ax.scatter(df[mask]['Ca'], df[mask]['Elevation'], label=secs[i], color=clr_dict[secs[i]], edgecolor='k', marker='D')

ax.set_xlim(-2.0, 1.5)
ax.set_ylim(-50, 400)
ax.legend(loc='upper left',frameon=False, ncol=1, fontsize=10)
ax.set_xlabel(r'$\delta^{44/40}$Ca (‰)', fontsize=14)
#ax.set_xlabel(r'$\delta^{44}$Ca/$\delta^{40}$Ca (‰)', fontsize=14)
ax.set_ylabel('Depth (m)', fontsize=14)
ax.grid(ls=':')

plt.savefig('Ca.pdf', bbox_inches='tight')


# In[ ]:




