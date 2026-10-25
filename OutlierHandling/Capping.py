def capping(df,col):
 
 q1=df[col].quantile(0.25)
 q3=df[col].quantile(0.75)

 IQR=q3-q1
 lower_bound=q1-1.5*IQR
 upper_bound=q3+1.5*IQR
 df[col]=df.clip(upper=upper_bound,lower=lower_bound)
 return df