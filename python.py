import pandas as pd
df = pd.read_csv('Super.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y') 
df['Month_Year'] = df['Order Date'].dt.strftime('%b-%Y')     # to change the month-year
print(df[['Order Date', 'Month_Year']].head())
df.to_csv('Super_clean.csv', index=False)