import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('Life Expectancy Data.csv')
print(df.head())
print(df.info())

# Drop unnecessary columns
df = df.drop(['Country', 'Infant deaths', 'Year', 'Status', 'under-five deaths', 'thinness 1-19 years', 'thinness 5-9 years'], axis=1)

# Remove missing values
df = df.dropna()

X = df.drop('Life expectancy', axis=1)
y = df['Life expectancy']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
print(f'R-squared: {score:.2f}')

with open('linear_regression_model.pkl', 'wb') as file:
    pickle.dump(model, file)
