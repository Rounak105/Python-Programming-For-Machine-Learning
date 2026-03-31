import pandas as pd
data={'Math':[90,85,80,95],
      'Science':[88,85,86,90],
      'English': [78,88,98,99]
      }
df=pd.DataFrame(data)
print("DataFrame: ")
print(df)

Correlation=df.corr()
print("\n Correlation Matrix: ")
print(Correlation)
