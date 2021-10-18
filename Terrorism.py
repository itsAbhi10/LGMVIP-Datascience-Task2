#!/usr/bin/env python
# coding: utf-8

# # Name:- Abhishek Ramesh Pawar
# ## Task:- Exploratory Data Analysis on Dataset - Terrorism (Intermediate Level)
# ### October 2021 Batch
# ### Data Science Intern at LetsGrowMore
# 

# * Importing important Libraries

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# * Read the dataset

# In[13]:


df = pd.read_csv(r'C:\\Users\\ap585\\Downloads\\globalterrorismdb_0718dist.csv', encoding='latin1')


# In[14]:


df


# In[15]:


df.head()


# In[16]:


df.tail()


# In[19]:


df.shape


# In[20]:


df.describe()


# In[21]:


df.corr()


# In[22]:


df.columns.values


# In[23]:


df.dtypes


# In[24]:


df.nunique()


# * Check for any NULL value

# In[25]:


df.isnull().sum()


# ** Plot the figure that shows null values present in Dataset

# In[26]:


plt.figure(figsize=(20,5))
sns.heatmap(df.isnull(), yticklabels=False)
plt.title("Hetmap of Null values Present in Dataset")


# * Finding out the missing values

# In[27]:


features_with_na=[features for features in df.columns if df[features].isnull().sum()>1]

for feature in features_with_na:
    print(feature, np.round(df[feature].isnull().mean(), 4), '% missing values')


# In[34]:


corr = df.corr()
plt.figure(figsize=(20,20))
sns.heatmap(data = corr, cmap = 'YlGnBu')
plt.title("Cmap for Dataset")
plt.show()


# #### Top 10 countries that have highest number of Attacks

# In[36]:


df['country_txt'].value_counts().index[:10]


# #### Top 5 region with highest number of Attacks

# In[38]:


df['region_txt'].value_counts().index[:5]


# #### Maximum no. of people killed by single attack

# In[39]:


print('Maximum no. of people that ere killed by single terrorist attack were',df['nkill'].max(),'peope, which tok place in Iraq')


# #### Top 10 countries with highest no. of deaths due to terrorist attacks

# In[40]:


people_died = df[["country_txt","nkill"]].groupby('country_txt').sum()
people_died.head(10)


# #### Plot the Bargraph for people died with respect to years 

# In[62]:


year = df["iyear"].unique()
years_count = df['iyear'].value_counts(dropna = False).sort_index()
plt.figure(figsize = (15,10))
sns.barplot(x = year, y = years_count, palette = 'tab10')
plt.xticks(rotation = 45)
plt.xlabel('Years', fontsize = 18)
plt.ylabel('Numbr of People Died', fontsize = 18)
plt.title('No. of People died V/S Years', fontsize=22)


# #### No. of people died based on attack type 

# In[46]:


attack_type = df[["attacktype1_txt","nkill"]].groupby('attacktype1_txt').sum()
attack_type.plot(kind='bar', colormap='inferno', figsize=(15,8))
plt.xlabel('Attack Type')
plt.ylabel('No. of People Died')
plt.title('No. of People Died V/S Attack Type', fontsize=20)


# #### No. of people Died based on Weapon used 

# In[48]:


weapon = df[["weaptype1_txt","nkill"]].groupby('weaptype1_txt').sum()
weapon.plot(kind='bar', colormap='inferno', figsize=(15,8))
plt.xlabel('Weapon used')
plt.ylabel('No. of People Died')
plt.title('No. of People Died V/S Weapon Used', fontsize=20)


# #### Top 10 Terrorist Group Attack 

# In[63]:


df['gname'].value_counts().to_frame().drop('Unknown').head(10).plot(kind='bar', color = 'orange', figsize = (20,12))
plt.xlabel("Terrorist Group name", fontsize = 18)
plt.ylabel("Attack Number", fontsize = 18)
plt.title("Top 10 Terrorist group attacks", fontsize = 22)
plt.show()


# #### * Terrorist attack by region in Each Year 

# In[70]:


pd.crosstab(df.iyear, df.region).plot(kind='area', figsize = (15,8))
plt.xlabel('Years', fontsize = 18)
plt.ylabel('No. Of Attaks', fontsize = 18)
plt.title('No. Of Attaks By Region', fontsize = 22)


# * Import Folium Library

# In[50]:


import folium
from folium.plugins import MarkerCluster


# In[55]:


filterYear = df['iyear'] == 2014
filterTerrorism = df[filterYear]

reqFilterTerrorism = filterTerrorism.loc[:, 'city':'longitude']
reqFilterTerrorism = reqFilterTerrorism.dropna()
reqFilterTerrorismList = reqFilterTerrorism.values.tolist()

map = folium.Map(location = [0, 30], titles = 'CartoDB Positron', zoom_start=2)

## Clustered Marker
markerCluster = folium.plugins.MarkerCluster().add_to(map)
for point in range(0, len(reqFilterTerrorismList)):
    folium.Marker(location = [reqFilterTerrorismList[point][1],reqFilterTerrorismList[point][2]], popup = reqFilterTerrorismList[point][0]).add_to(markerCluster)
map.save(r"C:\\Users\\ap585\\Downloads\\terror2014")
map


# In[72]:


data = df.pivot_table(columns= 'attacktype1_txt', values= 'nkill', aggfunc= 'sum')
data


# In[73]:


data1 = df.pivot_table(columns= 'country', values= 'nkill', aggfunc= 'sum')
data1


# #### Top 10 terror group with most number of Attacks

# In[75]:


df.gname.value_counts()[1:11]


# # Thank You!
