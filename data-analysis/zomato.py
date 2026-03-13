import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_csv('Zomato-data-.csv')

def handleRate(value):
    value=str(value).split('/')
    value=value[0];
    return float(value)

# type of rest
print(dataframe.head())
dataframe['rate']=dataframe['rate'].apply(handleRate)
sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")
plt.savefig('guest_count_per_type.jpg')

# number of votes
groupedData = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes':groupedData})
plt.plot(result, c='green', marker='o')
plt.xlabel('Type or restaurant')
plt.ylabel('Votes')
plt.savefig('view_by_votes.jpg')

# looking for most voted rest

max_votes = dataframe['votes'].max()
rmost = dataframe.loc[dataframe['votes'] == max_votes, 'name']
print('Most Voted')
print(rmost)

sns.countplot(x=dataframe['online_order'])
plt.savefig("online_orders.jpg")
