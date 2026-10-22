from scipy.stats import  zscore
def detect_outlier(df,col):
  values=df[col].dropna()
  z_scores=zscore(values)
  outliers=values[abs(z_scores)>3]
  return outliers

