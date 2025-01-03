import os
import sys
import dill  # Using dill for both saving and loading complex objects
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        # Using dill for better compatibility (optional)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for i in range(len(models)):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]

            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = {
                "train_score": train_model_score,
                "test_score": test_model_score,
                "best_params": gs.best_params_,
                "best_score": gs.best_score_
            }

        return report

    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        print(f"Attempting to load object from: {file_path}")  # Debug info
        if os.path.exists(file_path):
            if os.path.getsize(file_path) == 0:
                raise EOFError(f"The file {file_path} is empty.")
            with open(file_path, "rb") as file_obj:
                return dill.load(file_obj)
        else:
            raise FileNotFoundError(f"The file {file_path} does not exist.")
    except Exception as e:
        raise CustomException(e, sys)

