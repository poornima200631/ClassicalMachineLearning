import pandas as pd
import numpy as np
data={
  'male':[50,30,20],
  'female':[30,40,30]
}
a=0.05
contigency_Table=pd.DataFrame(data,index=['A','B','C'])
from scipy.stats import chi2_contingency
chi2,p_value,dof,expected=chi2_contingency(contigency_Table)
print("chi2=",chi2)
print("p_value=",p_value)
print("dof=",dof)
print("expected=",expected)
if p_value<=a:
  print("gender and product prefrence are related")
else:
  print("gender and product prefrence are not related")
