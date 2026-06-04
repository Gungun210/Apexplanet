import pandas as pd
import numpy as np

# =====================
# 1. LOAD DATA
# =====================
df = pd.read_csv('titanic.csv')
print("Original Shape:", df.shape)

# =====================
# 2. MISSING VALUES
# =====================

df['Age'] = df['Age'].fillna(df['Age'].median())
df['Fare'] = df['Fare'].fillna(df['Fare'].median())
# Cabin - itna missing hai (78%) to drop kar do column
df.drop(columns=['Cabin'], inplace=True)

print("Missing values after cleaning:")
print(df.isnull().sum())

# =====================
# 3. FEATURE ENGINEERING
# =====================

# AgeGroup column banana
df['AgeGroup'] = pd.cut(df['Age'], 
                         bins=[0, 12, 18, 35, 60, 100],
                         labels=['Child', 'Teen', 'Young Adult', 'Adult', 'Senior'])

# FamilySize column
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# IsAlone column
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

# FareCategory
df['FareCategory'] = pd.cut(df['Fare'],
                              bins=[0, 10, 30, 100, 600],
                              labels=['Low', 'Medium', 'High', 'Very High'])

print("\nNew columns added:")
print(df[['Age', 'AgeGroup', 'FamilySize', 'IsAlone', 'Fare', 'FareCategory']].head(10))

# =====================
# 4. STANDARDIZATION
# =====================

# Sex column encode karo
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# Embarked encode karo
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# =====================
# 5. OUTLIER CHECK
# =====================
Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Fare'] < Q1 - 1.5*IQR) | (df['Fare'] > Q3 + 1.5*IQR)]
print(f"\nFare outliers found: {len(outliers)}")

# =====================
# 6. SAVE CLEANED DATA
# =====================
df.to_csv('cleaned_titanic.csv', index=False)
print("\nCleaned dataset saved!")
print("Final Shape:", df.shape)