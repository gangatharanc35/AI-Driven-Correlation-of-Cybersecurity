import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

data = pd.read_csv("dataset.csv")

X = data[['login_attempts',
          'failed_logins',
          'transaction_amount',
          'new_device']]

model = IsolationForest(contamination=0.2)

model.fit(X)

joblib.dump(model,"model.pkl")

print("Model Saved Successfully")
