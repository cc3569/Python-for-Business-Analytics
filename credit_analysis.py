# Import necessary libraries
import pandas as pd

# Import dataframe
df = pd.read_csv('/content/credit.csv')

# Print descriptive statistics
print(df.describe().round(4))
print()

# Group by 'PAY_1' and print the mean for 'BILL_AMT1'
print(df.groupby('PAY_1')['BILL_AMT1'].mean())
print()

# Group by 'PAY_2' and print the mean for 'AGE'
print(df.groupby('PAY_2')['AGE'].mean())
print()

# View the number of unique ages in 'PAY_2' on the 'AGE' column when grouped by 'PAY_2'
print(df.groupby('PAY_2')['AGE'].nunique())
print()

# Take subsets of data, one for males and the other for females
male = df[df['SEX'] == 1]
female = df[df['SEX'] == 2]

# Apply .nunique() method to 'PAY_1' and 'PAY_6' for each subset
print(male[['PAY_1', 'PAY_6']].nunique())
print()
print(female[['PAY_1', 'PAY_6']].nunique())
print()

# Average Balances ('LIMIT_BAL') by 'SEX'
print("Average Balanaces by Sex:")
print(df.groupby('SEX')['LIMIT_BAL'].mean())
print()

# Average Balances ('LIMIT_BAL') by 'EDUCATION'
print("Average Balances by Education Level:")
print(df.groupby('EDUCATION')['LIMIT_BAL'].mean())
print()

# Average Balances ('LIMIT_BAL') by 'MARRIAGE'
print("Average Balances by Marital Status:")
print(df.groupby('MARRIAGE')['LIMIT_BAL'].mean())
print()
