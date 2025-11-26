import pandas as pd
df = pd.read_csv('employees_with_missing.csv')
df
df.isna()
df.isna().sum()
df.dropna()
df.salary = df.salary.fillna(value=df.salary.mean())
df
df.years_at_company = df.years_at_company.fillna(value=df.years_at_company.mean())
df
df.years_at_company = df.years_at_company.fillna(value=df.years_at_company.mean())
df
df.department = df.department.fillna(value = 'Unknown')
df