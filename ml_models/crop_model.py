import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load the dataset
data = pd.read_csv('ml_models/crop_dataset.csv')

# Input features
X = data.drop('label', axis=1)

# Output labels
y = data['label']

# Create and train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)


def predict_crop(n, p, k, temp, humidity, ph, rainfall):

    prediction = model.predict(
        [[
            float(n),
            float(p),
            float(k),
            float(temp),
            float(humidity),
            float(ph),
            float(rainfall)
        ]]
    )

    return prediction[0]