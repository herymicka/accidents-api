from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import bentoml

BASE_DIR = Path(__file__).resolve().parent.parent.parent
data_path = BASE_DIR / "data" / "preprocessed"

X_train = pd.read_csv(data_path / "X_train.csv")
X_test = pd.read_csv(data_path / "X_test.csv")
y_train = pd.read_csv(data_path / "y_train.csv")
y_test = pd.read_csv(data_path / "y_test.csv")

y_train = y_train.squeeze()
y_test = y_test.squeeze()

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy}")

# Sauvegarde locale
joblib.dump(model, BASE_DIR / "src/models/trained_model.joblib")

# 🔥 Sauvegarde BentoML (CORRECT POUR LE COURS)
model_ref = bentoml.sklearn.save_model("accidents_rf", model)

print(f"Modèle enregistré sous : {model_ref}")