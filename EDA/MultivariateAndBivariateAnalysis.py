import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import (
    pearsonr,
    spearmanr
)
df=pd.read_csv('titanic.csv')
numeric_cols=df.select_dtypes(include=np.number).columns.tolist()
numeric=df[numeric_cols]
categorical_cols=df.select_dtypes(include=['object', 'str', 'category']).columns.tolist()
categorical=df[categorical_cols]
print("pearson Relation:")
print(numeric.corr(method="pearson"))
# print("spearman Relation:")
# print(categorical.corr(method="spearman"))

plt.figure(figsize=(12,8))
sns.heatmap(numeric.corr(),annot=True,fmt=".2f",cmap="coolwarm")
plt.tight_layout()
plt.show()


for i,col1 in enumerate(numeric_cols):
  for col2 in numeric_cols[i+1:]:
    plt.figure(figsize=(8,6))
    sns.scatterplot(data=df,x=col1,y=col2)
    plt.tight_layout()
    plt.show()

for i,col1 in enumerate(categorical):
  for col2 in categorical[i+1:]:
    plt.figure(figsize=(8,6))
    sns.heatmap(data=df,x=col1,y=col2)
    sns.clustermap(data=df,x=col1,y=col2)
    plt.tight_layout()
    plt.show()


for col1 in categorical:
  for col2 in numeric:
    plt.figure(figsize=(8,6))
    sns.boxplot(data=df,x=col1,y=col2)
    plt.tight_layout()
    plt.show()

    