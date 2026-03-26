'''
Assignment (09/03/2026)

Assignment Name : House Price Predictor
Description : Train a Linear Regression model, 
predict prices, and test with new input.
'''

import pandas as pd

data = {
    "Area": [500, 800, 1000, 1200, 1500, 1800],
    "Price": [1000000, 1500000, 2000000, 2500000, 3000000, 3500000]
}

df = pd.DataFrame(data)

from sklearn.linear_model import LinearRegression

X = df[["Area"]]
y = df["Price"]

model = LinearRegression()
model.fit(X, y)


predicted_price = model.predict([[1300]])
print(predicted_price)
