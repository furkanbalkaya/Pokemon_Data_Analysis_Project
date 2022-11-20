
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



data = pd.read_csv("pokemon.csv")

data.head()

data.columns

data.shape

data.info()

data.nunique()

data.isnull().sum()

print(data['weight_kg'].value_counts(dropna=False))

print(data['percentage_male'].value_counts(dropna=False))

print(data['height_m'].value_counts(dropna=False))

data.describe()

data['height_m'].fillna(0.6,inplace=True)

data['percentage_male'].fillna(50,inplace=True)
data['weight_kg'].fillna(15,inplace=True)

data.isnull().sum()

corr=data.corr()
corr

ax=plt.figure(figsize=(20,20))
sns.heatmap(corr,annot=True,fmt="0.1")
plt.show()

data.groupby(['type1'])['speed'].mean().plot.bar(figsize=(8,8))

sns.boxplot(data=data,y='speed',x='is_legendary')

plt.figure(figsize=(8,8))
sns.boxplot(data=data,y='speed',x='is_legendary',hue='type1')
plt.legend(bbox_to_anchor=(1,1))

sns.distplot(data['speed'],kde=False)

new_data=data[data['speed']<160]

sns.distplot(new_data['speed'],kde=False)

tips=sns.load_dataset('tips')
tips.head()

sns.pairplot(tips)

sns.pairplot(tips,hue='sex')

