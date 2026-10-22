import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../EDA/titanic.csv")

for col in df.select_dtypes(include="number").columns:
  plt.figure(figsize=(6, 3))
  sns.boxplot(x=df[col])
  plt.figure(figsize=(6, 3))
  sns.histplot(x=df[col],kde=True)
  plt.tight_layout()
  plt.show()

