
# coding: utf-8

# In[292]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[293]:


mandi_data = pd.read_csv("CMO_MSP_Mandi.csv")


# In[294]:


mandi_data


# In[119]:


mandi_data.describe()


# In[295]:


mandi_data.isnull().sum()


# In[296]:


mandi_data[mandi_data.msprice.isnull()]


# Since the dataset is small, and is an yearly data, rather than removing the missing values, repopulating it will be a better option.
# Since the missing values are for the year 2016, we populate the missing values using the value of the year 2015, with the assumption that there is no change in the price of the commodity.

# In[318]:


temp = mandi_data.sort_values(by= ["commodity", "year"])


# In[319]:


temp['commodity'] = [i.lower() for i in temp.commodity.values]


# In[320]:


temp.head()


# In[321]:


temp = temp.fillna(method='ffill', limit=1)


# In[322]:


temp[temp.msprice.isnull()]


# MSPRICE for Soyabean_Black is an exception as the values for both 2015 and 2016 are missing.
# To populate it, we redo the forward fill method.

# In[323]:


temp = temp.fillna(method='ffill', limit=1)


# In[324]:


temp[temp.msprice.isnull()]


# In[303]:


ax = sns.boxplot(x="Type", y="msprice", data=temp, whis=1.5)


# In[304]:


aY = sns.boxplot(x="year", y="msprice", data=temp, whis=1.5)


# In[305]:


a = sns.boxplot(y="msprice", data=temp, whis=1.5)


# The boxplot shows that there are no outlier values in MSPrice. This is test enough for outlier detection.

# In[317]:


temp.head()


# In[309]:


temp.index = temp['year']
temp


# In[315]:


temp.year.unique()


# In[325]:


#print(df.loc[df['A'] == 'foo'])
#temp.loc[temp['year'] == 2014,2015,2016]
#temp.query('year == "2014", "2015", "2016"')
#temp[temp.year == 2014,2015,2016]
years = [2014,2015, 2016]
temp_years= temp[temp.year.isin(years)]


# In[326]:


temp_years.head()


# In[327]:


temp_years = temp_years.groupby(["commodity", "year"], as_index=False).mean()


# In[278]:


temp_years


# ### Understanding price fluctuation accounting to seasonal effect

# In[20]:


sns.tsplot(temp.loc[temp["commodity" ]== "bajri","msprice"])


# In[328]:


monthly_data = pd.read_csv("Monthly_data_cmo.csv")


# In[329]:


monthly_data


# In[330]:


monthly_data.describe()


# In[331]:


monthly_data.isnull().sum()


# In[332]:


monthly_data['Commodity'] = [i.lower() for i in monthly_data.Commodity.values]


# In[335]:


temp3 = monthly_data.groupby(["Commodity", "Year"], as_index=False).mean()


# In[336]:


temp_years


# In[338]:


u1 = set(temp_years.commodity.unique())
u1


# In[339]:


u2 = set(temp3.Commodity.unique())
u2


# In[345]:


print(list(temp3), len(temp3))
print(list(temp_years), len(temp_years))


# In[354]:


mergedData = pd.merge(left=temp3, right=temp_years, how='inner', left_on='Commodity', right_on='commodity')
len(mergedData)


# In[363]:


mergedData.head()


# In[368]:


#mergedData[['modal_price', 'commodity']].plot()
plt.subplot(211)
sns.barplot('modal_price', 'commodity', data=mergedData)
plt.subplot(212)
sns.barplot('msprice', 'commodity', data=mergedData)


# In[271]:


temp3.head()


# In[283]:


bool_com = [i in temp_years.commodity.unique() for i in u2.intersection(u1)]


# In[284]:


temp_years = temp_years.iloc[bool_com, :]


# In[289]:


temp_years.commodity.unique()


# In[286]:


bool_3 = [i in temp3.Commodity.unique() for i in u2.intersection(u1)]


# In[287]:


temp3 = temp3.iloc[bool_3, :]


# In[288]:


temp3.Commodity.unique()


# In[257]:


plt.rcParams['figure.figsize']=18,9


# In[290]:


sns.barplot('Commodity', 'modal_price', data=temp3)


# In[360]:


sns.barplot('Commodity', 'modal_price', data=mergedData)


# In[291]:


sns.barplot('commodity', 'msprice', data=temp_years)

