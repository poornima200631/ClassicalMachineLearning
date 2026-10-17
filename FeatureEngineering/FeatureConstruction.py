import pandas as pd
import numpy as np

def FeatureConstruction(df):
    df=df.copy()
    df['FamilySize']=df['SibSp']+df['Parch']+1
    df['IsAlone']=(df['FamilySize']==1).astype(int)
    df['AgeFareInteraction']=df['Age']*df['Fare']
    df['FarePerPerson']=df['Fare']/df['FamilySize']
    df["FamilyCategory"] = np.select(
    [
        df["FamilySize"] == 1,
        df["FamilySize"].between(2, 4),
        df["FamilySize"] >= 5
    ],
    [
        "Alone",
        "SmallFamily",
        "LargeFamily"
    ],
    default="Unknown"
   )
    return df
    
