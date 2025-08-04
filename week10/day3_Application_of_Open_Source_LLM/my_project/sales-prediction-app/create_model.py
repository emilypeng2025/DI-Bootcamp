import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
import pickle

# --- Dummy Training Data ---
data = pd.DataFrame({
    "store_nbr": [1, 2, 3, 4],
    "family": ["BEAUTY", "AUTOMOTIVE", "BEAUTY", "GROCERY"],
    "onpromotion": [2, 1, 0, 3],
    "transactions": [200, 150, 120, 300],
    "cluster": [1, 2, 1, 3],
    "sales": [1000, 1500, 1200, 2000]
})

categorical_cols = ["family"]
numerical_cols = ["store_nbr", "onpromotion", "transactions", "cluster"]

# --- Imputers ---
num_imputer = SimpleImputer(strategy="mean")
cat_imputer = SimpleImputer(strategy="most_frequent")

data[categorical_cols] = cat_imputer.fit_transform(data[categorical_cols])
data[numerical_cols] = num_imputer.fit_transform(data[numerical_cols])

# --- Encoder ---
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
encoded_cats = encoder.fit_transform(data[categorical_cols])
encoded_cat_df = pd.DataFrame(encoded_cats, columns=encoder.get_feature_names_out(categorical_cols))

# --- Combine features ---
final_features = pd.concat([data[numerical_cols], encoded_cat_df], axis=1)

# --- Train model ---
model = RandomForestRegressor()
model.fit(final_features, data["sales"])

# --- Save components ---
components = {
    "num_imputer": num_imputer,
    "cat_imputer": cat_imputer,
    "encoder": encoder,
    "model": model
}

with open("rf_model.pkl", "wb") as f:
    pickle.dump(components, f)

print("✅ Model saved to rf_model.pkl")
