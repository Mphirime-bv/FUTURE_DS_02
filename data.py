import pandas as pd

df = pd.read_csv('telco_clean.csv')

df['Churn_Binary'] = df['Churn'].map({'Yes': 1, 'No': 0})

df['Tenure_Group'] = pd.cut(df['tenure'],
    bins=[0, 12, 24, 48, 72],
    labels=['0-12 months', '13-24 months', '25-48 months', '49-72 months'])

df.to_csv('telco_final.csv', index=False)