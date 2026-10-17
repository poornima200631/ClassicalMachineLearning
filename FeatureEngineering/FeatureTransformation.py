import pandas as pd 
import numpy as np
def FeatureTransformation(df):
   df=df.copy()
   df['FareLog']=np.log1p(df['Fare'])
   df['Faresqrt']=np.sqrt(df['Fare'])
   df['FareReciprocal']=1/(df['Fare'].replace(0,np.nan))
   return df