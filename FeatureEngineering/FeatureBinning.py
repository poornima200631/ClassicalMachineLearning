import pandas as pd
def FeatureBinning(df):
  df=df.copy()
  df['AgeGroup']=pd.cut(df['Age'],bins=[0,12,18,35,60,100],labels=['Child','Teenager','Young Adult','Adult','Old'],include_lowest=True)
  df['FareGroup']=pd.cut(df['Fare'],bins=4,labels=['low','medium','high','very high'])
  df['FareEqualFrequency']=pd.cut(df['Fare'],bins=4 ,labels=["Q1", "Q2", "Q3", "Q4"],
        duplicates="drop")
  return df