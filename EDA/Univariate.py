import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('titanic.csv')
print(df.shape)
print(df.head())
print(df.tail())
print('rows',df.shape[0])
print('columns',df.shape[1])
print(df.describe())
print(df.sample(min(5,len(df))))
print(df.columns.tolist())
print(df.index)
print(df.dtypes)
print(df.info())
print(df.describe(include="all"))



print(df.isnull().sum().sort_values(ascending=False))
print((df.isnull().mean()*100).round(2).sort_values(ascending=False))
print(df.duplicated().sum())
print(df.nunique().sum())
print(df.columns[df.nunique()==1].tolist())
print(df.select_dtypes(include=np.number).columns.tolist())

numeric_cols=df.select_dtypes(include=np.number).columns.tolist()
numeric=df[numeric_cols]
print(numeric.mean())
print(numeric.quantile(0.25))
print(numeric.quantile(0.75))
print('iqr: ',numeric.quantile(0.75)-numeric.quantile(0.25))
print(numeric.skew())
print(numeric.kurtosis())

categorical_cols=df.select_dtypes( include=['object', 'str', 'category']).columns.tolist()
catego=df[categorical_cols]
for col in catego:
    print(col.upper())
    print(df[col].value_counts())
    print(df[col].nunique())


for col in numeric:
    fig,axes=plt.subplots(1,2,figsize=(12,4))
    sns.histplot(data=df, x=col, kde=True, ax=axes[0],bins=50)
    axes[0].set_title('Histogram of {col}')

    sns.boxplot(data=df,x=col,ax=axes[1])
    axes[1].set_title('Boxplot of {col}')

    plt.tight_layout()
    plt.show()
  

for col in catego:
    counts = df[col].astype("object").fillna("Missing").value_counts()
    plt.figure(figsize=(10,6))
    sns.barplot(x=counts.index,y=counts.values)
    plt.title('Barplot ')
    plt.xlabel(col)
    plt.ylabel('freq')
    plt.tight_layout()
    plt.show()


for col in numeric:
    series = df[col].dropna()

    if series.empty:
        continue

    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)

    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    outliers = series[(series < lower) | (series > upper)]
    print('outliers')
    print(outliers)