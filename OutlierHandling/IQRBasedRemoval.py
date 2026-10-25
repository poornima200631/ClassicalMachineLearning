def removeOutlier(df,col):
  df=df.copy()


  q1=df[col].quantile(0.25)
  q3=df[col].quantile(0.75)
  IQR = q3 - q1

  lower_bound = q1 - 1.5 * IQR
  upper_bound = q3 + 1.5 * IQR


  mask=(
    df[col].isna()|(
       (df[col] >= lower_bound) &
     (df[col] <= upper_bound)
    )
  )
  df=df[mask]
  return df