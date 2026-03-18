import joblib
import numpy as np
import bentoml

@bentoml.service
class AccidentClassifier:
    def __init__(self) -> None:
        self.model = joblib.load("src/models/trained_model.joblib")

    @bentoml.api
    def predict(self, input_data: np.ndarray) -> np.ndarray:
        input_data = np.array(input_data)
        if input_data.ndim == 1:
            input_data = input_data.reshape(1, -1)
        prediction = self.model.predict(input_data)
        return prediction
