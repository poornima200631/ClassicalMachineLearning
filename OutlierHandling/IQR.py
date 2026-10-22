def detect_Outlier_IQR(df,col):
  values=df[col].dropna()

  q1=values.quantile(0.25)
  q3=values.quantile(0.75)

  IQR=q3-q1
  lower_bound=q1-1.5*(IQR)
  upper_bound=q3+1.5*(IQR)
  outliers=values[(values<lower_bound)|(values>upper_bound)]
  return outliers