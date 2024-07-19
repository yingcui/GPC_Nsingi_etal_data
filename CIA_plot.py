#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle

import numpy as np
import matplotlib.gridspec as gridspec


# In[2]:


df = pd.read_csv('/glade/work/jnsingi/Permian-data/CIA_plot.csv')
df


# In[3]:


secs = list(set(df['Section']))
secs


# In[13]:


# Corrected Chemical Index of Alteration "CIAcorr"

clr_dict = {
    'Shuiyuguan section': 'lime',
    'Dalongkou section': 'fuchsia',
}

fig, ax = plt.subplots()

for i in range(len(secs)):
    mask = df["Section"]==secs[i]
    ax.scatter(df[mask]['CIAcorr.'], df[mask]['Elevation (m)'], label=secs[i], color=clr_dict[secs[i]], edgecolor='k', marker='D')

ax.set_xlim(50, 90)
ax.set_ylim(-400, 800)
ax.legend(loc='upper left',frameon=False, ncol=1, fontsize=10)
ax.set_xlabel(r'CIAcorr', fontsize=14)
ax.set_ylabel('Depth (m)', fontsize=14)
ax.grid(ls=':')

#plt.savefig('CIAcorr.pdf', bbox_inches='tight')


# In[5]:


# Chemical Index of Alteration "CIA"

clr_dict = {
    'Shuiyuguan section': 'darkorange',
    'Dalongkou section': 'cyan',
}

fig, ax = plt.subplots()

for i in range(len(secs)):
    mask = df["Section"]==secs[i]
    ax.scatter(df[mask]['CIA'], df[mask]['Elevation (m)'], label=secs[i], color=clr_dict[secs[i]], edgecolor='k', marker='D')

ax.set_xlim(50, 90)
ax.set_ylim(-400, 800)
ax.legend(loc='upper left',frameon=False, ncol=1, fontsize=10)
ax.set_xlabel(r'CIA', fontsize=14)
ax.set_ylabel('Depth (m)', fontsize=12)
ax.grid(ls=':')

#plt.savefig('CIA.pdf', bbox_inches='tight')


# In[6]:


# Weathering Index of Parker "WIP"

clr_dict = {
    'Shuiyuguan section': 'lawngreen',
    'Dalongkou section': 'deepskyblue',
}

fig, ax = plt.subplots()

for i in range(len(secs)):
    mask = df["Section"]==secs[i]
    ax.scatter(df[mask]['WIP'], df[mask]['Elevation (m)'], label=secs[i], color=clr_dict[secs[i]], edgecolor='k', marker='D')

ax.set_xlim(10, 80)
ax.set_ylim(-400, 1000)
ax.legend(loc='upper left',frameon=False, ncol=1, fontsize=10)
ax.set_xlabel(r'WIP', fontsize=14)
ax.set_ylabel('Depth (m)', fontsize=10)
ax.grid(ls=':')

#plt.savefig('WIP.pdf', bbox_inches='tight')


# In[ ]:




