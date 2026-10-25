def PercentileBased(df,col):
  values=df[col].dropna()
  lower_bound=values.quantile(0.01)
  upper_bound=values.quantile(0.99)

  outliers=values[(values<lower_bound)|(values>upper_bound)]

  return outliers