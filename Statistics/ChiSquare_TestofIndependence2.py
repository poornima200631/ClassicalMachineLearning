import pandas as pd
import numpy as np
data={
  'Onine':[45,15],
  'Classroom':[35,25],
  'Hybrid':[50,10]
}
a=0.05
Contingency_table=pd.DataFrame(data,index=['Passed','Fail'])
from scipy.stats import chi2_contingency
chi2,p_value,dof,expected=chi2_contingency(Contingency_table)
print("chi2=",chi2)
print("pvalue=",p_value)
print("dof=",dof)
print("expected=",expected)
if p_value<=a:
  print("Mode of Program is associated with the result of employee")
else:
  print("Mode of program is not associated with the result of employee")