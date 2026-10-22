import pandas as pd
def randomImputer(df,columns,random_state=42):
  df=df.copy()
 

  for col in columns:
     missing_mask=df[col].isnull()
     missing_values=df[col].isnull().sum()
     if missing_values==0:
       continue
     
     observed=df.loc[~missing_values,col]
     sample_values=observed.sample(n=missing_values,replace=True,random_state=random_state)

     df.loc[missing_mask,col]=sample_values.to_numpy()

  return df





  
