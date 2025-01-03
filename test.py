from src.utils import load_object
import pandas as pd

model_path = "/Users/ghanagokulgabburi/Documents/Python/mlproject/artifacts/model.pkl"
preprocessor_path = "/Users/ghanagokulgabburi/Documents/Python/mlproject/artifacts/proprocessor.pkl"

model = load_object(model_path)
preprocessor = load_object(preprocessor_path)

test_data = pd.DataFrame({...})  # Replace with sample input
#scaled_data = preprocessor.transform(test_data)
##predictions = model.predict(scaled_data)
#print(predictions)
