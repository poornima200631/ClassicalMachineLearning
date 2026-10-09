import pandas as pd
import numpy as np
data={
  'Traditional':[65,70,68,64,67],
  'Online':[75,78,72,80,76],
  'Hybrid':[80,85,82,88,84]
}
alpha=0.05
from scipy.stats import f_oneway
f,p=f_oneway(data['Traditional'],data['Online'],data['Hybrid'])
if p<=alpha:
  print("Reject h0 :means are not equal and course affect score")
else:
  print("Fail to reject h0:means are qual and course does not affect score")

trad_mean=np.mean(data['Traditional'])
online_mean=np.mean(data['Online'])
hybrid_mean=np.mean(data['Hybrid'])
print("Mean of Traditional:",trad_mean)
print("Mean of Online:",online_mean)
print("Mean of Hybrid:",hybrid_mean)