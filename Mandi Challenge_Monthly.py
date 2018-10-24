
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=18,9
import seaborn as sns


# In[3]:


monthly_data = pd.read_csv("Monthly_data_cmo.csv")
monthly_data.head()


# In[4]:


monthly_data.describe()


# In[6]:


monthly_data.isnull().sum()


# In[5]:


a = sns.boxplot(y="modal_price", data=monthly_data, whis=1.5)


# In[8]:


from scipy.stats import iqr


# In[6]:


Q1 = monthly_data.modal_price.quantile(0.25)
Q3 = monthly_data.modal_price.quantile(0.75)
IQR = Q3 - Q1
print(IQR)


# In[7]:


monthly_data.loc[monthly_data['modal_price'] < (Q1 - 1.5 * IQR), 'modal_price']
monthly_data.loc[~(monthly_data['modal_price'] > (Q3 + 1.5 * IQR)), 'modal_price']


# In[13]:


from datetime import datetime
monthly_data['date'] = pd.to_datetime(monthly_data['date'])
monthly_data.index = monthly_data['date']

#The data is not sorted by date and also the date is repetitive for each commodity for each apmc
monthly_data.sort_values(by='date', inplace=True)
monthly_data.head()


# In[14]:


monthly_data['Commodity'] = [i.lower() for i in monthly_data.Commodity.values]


# <h3>Plotting a time series plot for a region does not give fruitful results as a specific region may have many commodities, and hence will not give genuine insights</h3>

# In[9]:


sns.tsplot(monthly_data.loc[monthly_data["APMC" ]== "Ahmednagar","modal_price"])


# Firstly check which apmc has high frequency and also check frequency for the commodities in that region

# In[10]:


monthly_data.APMC.value_counts()


# In[41]:


monthly_data.query('APMC == "Mumbai"').Commodity.value_counts()


# In[11]:


from statsmodels.tsa.seasonal import seasonal_decompose


# In[15]:


monthly_data.query('APMC == "Mumbai" & Commodity == "coconut"').modal_price.plot()


# In[16]:


result = seasonal_decompose(monthly_data.query('APMC == "Ahmednagar" & Commodity == "bajri"').modal_price, model='additive', freq=1)
print("Seasonality: ",result.seasonal.plot())


# In[42]:


monthly_data.query('APMC == "Pune"').Commodity.value_counts()


# In[65]:


result = seasonal_decompose(monthly_data.query('APMC == "Pune" & Commodity == "pavtta"').modal_price, model='additive', freq=1)
print("Seasonality: ",result.seasonal.plot())


# In[43]:


monthly_data.query('APMC == "Satara"').Commodity.value_counts()


# In[66]:


result = seasonal_decompose(monthly_data.query('APMC == "Satara" & Commodity == "garlic"').modal_price, model='additive', freq=1)
print("Seasonality: ",result.seasonal.plot())


# <h3>The seasonality cannot be seen per commodity for a particular region as the data points are less that way.
# So, we take sum of all commodities for a region and check monthly seasonality.</h3>

# In[17]:


result = seasonal_decompose(monthly_data.query('APMC == "Mumbai"').groupby("date").sum().modal_price, model='additive', freq=12)
print("Seasonality: ",result.seasonal.plot())


# In[32]:


result = seasonal_decompose(monthly_data.query('APMC == "Pune"').groupby("date").sum().modal_price, model='additive', freq=12)
print("Seasonality: ",result.seasonal.plot())


# In[18]:


result = seasonal_decompose(monthly_data.query('APMC == "Nagpur"').groupby("date").sum().modal_price, model='additive', freq=12)
print("Seasonality: ",result.seasonal.plot())


# In[34]:


result = seasonal_decompose(monthly_data.query('APMC == "Barshi"').groupby("date").sum().modal_price, model='additive', freq=12)
print("Seasonality: ",result.seasonal.plot())


# In[19]:


result = seasonal_decompose(monthly_data.query('APMC == "Jalgaon"').groupby("date").sum().modal_price, model='additive', freq=12)
print("Seasonality: ",result.seasonal.plot())


# In[20]:


result = seasonal_decompose(monthly_data.query('APMC == "Solapur"').groupby("date").sum().modal_price, model='additive', freq=12)
print("Seasonality: ",result.seasonal.plot())


# After looking at seasonality accross APMC's for all commodities, we look at seasonality for top 5 commodities, accross the state.

# In[44]:


monthly_data.Commodity.value_counts()


# In[56]:


result = seasonal_decompose(monthly_data.query('Commodity == "gram"').groupby("date").sum().modal_price, model='additive', freq=12)
print("Seasonality: ",result.seasonal.plot())


# In[68]:


result = seasonal_decompose(monthly_data.query('Commodity == "wheat(husked)"').groupby("date").sum().modal_price, model='additive', freq=12)
print("Seasonality: ",result.seasonal.plot())


# In[57]:


result = seasonal_decompose(monthly_data.query('Commodity == "soybean"').groupby("date").sum().modal_price, model='additive', freq=12)
print("Seasonality: ",result.seasonal.plot())


# In[58]:


result = seasonal_decompose(monthly_data.query('Commodity == "sorgum(jawar)"').groupby("date").sum().modal_price, model='additive', freq=12)
print("Seasonality: ",result.seasonal.plot())


# In[23]:


result = seasonal_decompose(monthly_data.query('Commodity == "pigeon pea (tur)"').groupby("date").sum().modal_price, model='additive', freq=12)
print("Seasonality: ",result.seasonal.plot())


# In all seasonality graphs, it is evident that the seasonality is yearly and is dependent on the type of crop the commodity is. Some crops which are grown in the Rabi or summer season, such as Jawar, are then harvested in the winter season and sold then, indicating a price hike in the winter months. 
# 
# Similarly, there are crops such as Tur, are kharif crops grown during the rainy season, which lasts from June to October, post which we can see a hike in prices as the commodity reaches the market.

# In[59]:


result = seasonal_decompose(monthly_data.query('Commodity == "gram"').groupby("date").sum().modal_price, model='additive', freq=12)
print("Seasonality: ",result.observed.plot())


# Looking at the trend and observed line plot of the commodities, we can safely conclude that the seasonality type is neither additive nor multiplicative and is irrespective of the model chosen for decomposing.

# In[55]:


deseasonsoy = monthly_data.query('Commodity == "soybean"').groupby("date").sum().modal_price.pct_change()
result = seasonal_decompose(deseasonsoy.iloc[1:], model='additive', freq=12)
print("Seasonality: ",result.seasonal.plot())


# In[73]:


deseasongram = monthly_data.query('Commodity == "gram"').groupby("date").sum().modal_price.pct_change()
result = seasonal_decompose(deseasongram.iloc[1:], model='additive', freq=12)
print("Seasonality: ",result.trend.plot())


# In[72]:


deseasonwheat = monthly_data.query('Commodity == "wheat(husked)"').groupby("date").sum().modal_price.pct_change()
result = seasonal_decompose(deseasonwheat.iloc[1:], model='additive', freq=12)
print("Seasonality: ",result.trend.plot())


# In[ ]:


plt.subplot(221)
#plt.subplot(211)
result = seasonal_decompose(monthly_data.query('Commodity == "soybean"').groupby("date").sum().modal_price, model='additive', freq=12)
(seasonal_decompose(deseason.iloc[1:], model='additive', freq=12)
plt.plot(result.observed)
plt.subplot(222)
plt.plot(result.seasonal)


# In[79]:


seasonal_decompose(monthly_data.query('Commodity == "soybean"').groupby("date").sum().modal_price, model='additive', freq=12)

