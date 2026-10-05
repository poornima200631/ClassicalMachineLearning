import pandas as pd
import numpy as np
old_training = [
    42, 45, 39, 41, 44, 40, 43, 46, 38, 42,
    41, 44, 40, 43, 39
]
new_training = [
    38, 40, 36, 39, 37, 41, 35, 38, 36, 40,
    37, 39, 35, 38, 36
]
old_arr=np.array(old_training)
new_arr=np.array(new_training)
diff_data=old_arr-new_arr
n=len(diff_data)
m=np.mean(diff_data)
s=np.std(diff_data)
t_value=m/(s/np.sqrt(n))
from scipy.stats import shapiro
p=shapiro(diff_data).pvalue
if p>0.05:
  print("Normally distributed")
else:
  print("Not normally distributed")
print(t_value)

from scipy.stats import t
df=n-1
cdf_value=t.cdf(-1*t_value,df)
if cdf_value>0.05:
  print("No diff between average time after training program")
else:
  print("there is a diff between average time after training program")