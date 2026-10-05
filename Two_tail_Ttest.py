import pandas as pd
import numpy as np
delivery_time = [
    32, 28, 35, 31, 29, 34, 27, 30, 33, 36,
    31, 29, 28, 34, 32, 30, 37, 26, 31, 33,
    29, 35, 30, 28, 34, 32, 27, 31, 36, 29
]
arr_data=np.array(delivery_time)
n=len(arr_data)
import statistics as stt
s=stt.stdev(delivery_time)
m=stt.mean(delivery_time)
t_value=(m-30)/(s/np.sqrt(n))
from scipy.stats import shapiro
df=n-1
p=shapiro(arr_data).pvalue
if p>0.05:
  print("Data is normally distributed")
else:
  print("Data is not normally distributed")
print(t_value)
from scipy.stats import t
cdf__value=t.cdf(-1*t_value,df)
p_value=2*cdf__value
alpha=0.05
if p_value <= alpha:
  print("Reject the company's claim that the average delivery time is 30 minutes")
else:
  print("Fail to reject the company's claim that the average delivery time is 30 minutes")