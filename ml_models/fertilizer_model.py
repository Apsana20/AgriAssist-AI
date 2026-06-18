import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
data = pd.read_csv('ml_models/fertilizer_dataset.csv')

# Convert crop names to numbers
crop_encoder = LabelEncoder()
data['crop_name'] = crop_encoder.fit_transform(data['crop_name'])

# Input features
X = data.drop('label', axis=1)

# Output labels
y = data['label']

# Create and train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)


def predict_fertilizer(n, p, k, crop_name):

    crop_name = crop_name.lower()

    crop_value = crop_encoder.transform([crop_name])[0]

    prediction = model.predict(
        [[
            float(n),
            float(p),
            float(k),
            crop_value
        ]]
    )

    return prediction[0]