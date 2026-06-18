import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv('ml_models/yield_dataset.csv')

# Input features
X = data[['Area', 'Rainfall', 'Temperature']]

# Output
y = data['Yield']

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)


def predict_yield(area, rainfall, temperature):

    prediction = model.predict(
        [[
            float(area),
            float(rainfall),
            float(temperature)
        ]]
    )

    return f"{round(prediction[0], 2)} tons/hectare"