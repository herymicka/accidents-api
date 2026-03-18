import bentoml
import pandas as pd

@bentoml.service
class RFClassifierService:

    def __init__(self):
        self.model = bentoml.sklearn.load_model("accidents_rf:latest")

    @bentoml.api
    def predict(self, input_data: dict) -> dict:
        df = pd.DataFrame([input_data])
        prediction = self.model.predict(df)
        return {"prediction": prediction.tolist()}