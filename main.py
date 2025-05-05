# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import joblib
# import numpy as np

# # Load your models
# models = {
#     "randomforest": joblib.load("models/tuned_random_forest.pkl"),
#     # Add more if needed
#     "xgboost": joblib.load("models/tuned_xgboost.pkl")
# }

# # Define input schema
# class InputData(BaseModel):
#     LIMIT_BAL: float
#     PAY_0: int
#     PAY_2: int
#     PAY_3: int
#     PAY_4: int
#     PAY_5: int
#     PAY_6: int
#     PAY_AMT1: float
#     PAY_AMT2: float
#     PAY_AMT4: float
#     model: str

# app = FastAPI()

# @app.post("/predict")
# def predict(data: InputData):
#     try:
#         model = models.get(data.model)
#         if not model:
#             raise ValueError(f"Model '{data.model}' not found.")

#         # Convert input to 2D array
#         features = np.array([[
#             data.LIMIT_BAL, data.PAY_0, data.PAY_2, data.PAY_3, data.PAY_4,
#             data.PAY_5, data.PAY_6, data.PAY_AMT1, data.PAY_AMT2, data.PAY_AMT4
#         ]])

#         prediction = model.predict(features)[0]
#         return {"prediction": int(prediction)}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Map model names to their corresponding files
models = {
    "tuned_random_forest": joblib.load("models/tuned_random_forest.pkl"),
    "tuned_xgboost": joblib.load("models/tuned_xgboost.pkl")
}

# Define request schema
class InputData(BaseModel):
    LIMIT_BAL: float
    PAY_0: int
    PAY_2: int
    PAY_3: int
    PAY_4: int
    PAY_5: int
    PAY_6: int
    PAY_AMT1: float
    PAY_AMT2: float
    PAY_AMT4: float
    model: str

app = FastAPI()

@app.post("/predict")
def predict(data: InputData):
    try:
        model = models.get(data.model)
        if not model:
            raise ValueError(f"Model '{data.model}' not found. Available models: {list(models.keys())}")

        # Format features as expected by model
        features = np.array([[
            data.LIMIT_BAL, data.PAY_0, data.PAY_2, data.PAY_3, data.PAY_4,
            data.PAY_5, data.PAY_6, data.PAY_AMT1, data.PAY_AMT2, data.PAY_AMT4
        ]])

        prediction = model.predict(features)[0]
        return {"prediction": int(prediction)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
