#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df = pd.read_csv('/glade/work/jnsingi/Permian-data/d26Mg_scatter-plot.csv')
df = df.dropna(subset='Section')
df


# In[3]:


secs = list(set(df['Section']))
secs


# In[4]:


mask = df["Section"]==secs[0]
df[mask]


# In[5]:


clr_dict = {
    'Zal section': 'yellow',
    'Dajiang section': 'blue',
    'GK-1 core': 'red',
    'Zuodeng section': 'green',
    'Yanggudong section': 'orange',
}

fig, ax = plt.subplots()

for i in range(len(secs)):
    mask = df["Section"]==secs[i]
    ax.scatter(df[mask]['d26Mg.1'], df[mask]['Depthm'], label=secs[i], color=clr_dict[secs[i]], edgecolor='k')

ax.fill_betweenx(y=(-100, 800), x1=0., x2=0.5, color='blue', alpha=0.1)
ax.set_ylim(-100, 800)
ax.legend(frameon=False, ncol=2, fontsize=9)
ax.set_xlabel(r'$\delta^{26}$Mg permil')
ax.set_ylabel('Depth (m)')
ax.grid(ls=':')
ax.axhline(y=300, color='k')
ax.text(1.05, 0.6, 'Permian', transform=ax.transAxes, rotation='vertical')
ax.text(1.05, 0.2, 'Triassic', transform=ax.transAxes, rotation='vertical')

mask = (df['Section']==secs[0]) & (df['Depthm']==718.5)
pt = df[mask][['d26Mg.1', 'Depthm']].values[0]
print(pt)
print(len(pt))


# In[6]:


clr_dict = {
    'Zal section': 'yellow',
    'Dajiang section': 'aqua',
    'GK-1 core': 'red',
    'Zuodeng section': 'green',
    'Yanggudong section': 'orange',
}

fig, ax = plt.subplots()

for i in range(len(secs)):
    mask = df["Section"]==secs[i]
    ax.scatter(df[mask]['d26Mg.1'], df[mask]['Depthm'], label=secs[i], color=clr_dict[secs[i]], edgecolor='k', marker='D')
ax.set_xlim(-3.0, 1.5)
ax.set_ylim(-100, 800)
ax.legend(frameon=False, ncol=1, fontsize=9)
ax.set_xlabel(r'$\delta^{26}$Mg (‰)', fontsize=14)
ax.set_ylabel('Depth (m)', fontsize=14)
ax.grid(ls=':')

plt.savefig('Mg.pdf', bbox_inches='tight')


# In[ ]:




