import pandas as pd

def missing_report(df):
  missing_count=df.isnull().sum()
  missing_percentage=(missing_count/len(df)*100).round(2)

  report=pd.DataFrame({
    "Missing Count":missing_count,
    "Missing Percentage":missing_percentage
  })

  report=report[report["Missing Count"]>0].sort_values(by="Missing Percentage",ascending=False)
  print(report)



def handle_missing_values(report,df):
    df=df.copy()
    for col in report.index:
       if df[col].isnull().sum()==0:
          continue
       
       missing_percent=df[col].isnull().mean()*100
       
       if missing_percent>50:
          print(f"Dropping column {col} due to high missing percentage")
          df=df.drop(columns=[col])
          continue
       
       if pd.api.types.is_numeric_dtype(df[col]):
          skewness=df[col].skew()

          if abs(skewness)>1:
             value=df[col].median()
             df[col]=df[col].fillna(value)

          else:
             value=df[col].mean()
             df[col]=df[col].fillna(value)

       else:
          unique_count=df[col].nunique()
          unique_ratio = unique_count / max(df[col].notna().sum(), 1)

          if missing_percent>30:
             df[col]=df[col].fillna("Missing")
          elif unique_ratio < 0.5:
                mode_values = df[col].mode()

                if not mode_values.empty:
                    df[col] = df[col].fillna(mode_values[0])
                    print(f"{col}: Filled with mode ({mode_values[0]})")
                else:
                    df[col] = df[col].fillna("Unknown")
          else:
             df[col] = df[col].fillna("Unknown")
             print(f"{col}: Filled with Unknown")

    return df
