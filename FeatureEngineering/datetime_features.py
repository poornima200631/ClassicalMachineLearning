import pandas as pd
def DateTime(df,date_col):
  df=df.copy()
  df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
  df['date']=df[date_col].dt.date
  df['month']=df[date_col].dt.month
  df['day']=df[date_col].dt.day
  df['dateofweek']=df[date_col].dt.dayofweek
  df['quarter']=df[date_col].dt.quarter
  df['isWeekend']=(
    df['dateofweek'].dt.dayofweek>=5
  ).astype("Int64")
  return df