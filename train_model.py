import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("data/drug_repurposing_data.csv")

# Features
X = df.drop("disease", axis=1)

# Target
y = df["disease"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier()

# Train
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "models/repurposing_model.pkl")

print("Model trained and saved successfully!")