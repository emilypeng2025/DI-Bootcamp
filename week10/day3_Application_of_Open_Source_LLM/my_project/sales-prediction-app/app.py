import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

st.title("Sales Prediction Web App")
st.caption("Enter the details below to predict sales for a store and product family.")

# Load the trained model components
with open("rf_model.pkl", "rb") as f:
    components = pickle.load(f)

num_imputer = components["num_imputer"]
cat_imputer = components["cat_imputer"]
encoder = components["encoder"]
model = components["model"]

# Initialize the scaler (used later)
scaler = StandardScaler()

# --- UI: Title and Caption ---
st.title("Sales Prediction Web App")
st.caption("Enter the details below to predict sales for a store and product family.")

# --- Sidebar Descriptions ---
st.sidebar.header("Description of Input Fields")
st.sidebar.markdown("**Store Number**: ID of the store (0–54)")
st.sidebar.markdown("**Product Family**: e.g., 'AUTOMOTIVE', 'BEAUTY', etc.")
st.sidebar.markdown("**Items on Promotion**: Number of items currently on promotion")
st.sidebar.markdown("**State**: Ecuadorian province of the store")
st.sidebar.markdown("**Store Type**: Store classification (A, B, C, D, E)")
st.sidebar.markdown("**Cluster**: Store cluster number (1–17)")
st.sidebar.markdown("**Transactions**: Total transactions")
st.sidebar.markdown("**Date Features**: Month, Day, Day of Week")

# --- Input Fields ---
input_data = {}

col1, col2, col3 = st.columns(3)

with col1:
    input_data["store_nbr"] = st.slider("Store Number", 0, 54)
    input_data["family"] = st.selectbox("Product Family", [
        "AUTOMOTIVE", "BEAUTY", "BEVERAGES", "BOOKS", "BREAD/BAKERY", "CLEANING",
        "DAIRY", "DELI", "EGGS", "FROZEN FOODS", "GROCERY I", "GROCERY II",
        "HARDWARE", "HOME AND KITCHEN I", "HOME AND KITCHEN II", "LADIESWEAR",
        "LINGERIE", "LIQUOR,WINE,BEER", "MEATS", "PERSONAL CARE", "PET SUPPLIES",
        "PLAYERS AND ELECTRONICS", "POULTRY", "PREPARED FOODS", "PRODUCE", "SCHOOL AND OFFICE SUPPLIES",
        "SEAFOOD", "SNACK FOODS", "STATIONERY"]
    )
    input_data["onpromotion"] = st.number_input("Items on Promotion", 0, 1000)

with col2:
    input_data["state"] = st.selectbox("State", [
        'Pichincha', 'Cotopaxi', 'Chimborazo', 'Imbabura', 'Santo Domingo de los Tsachilas',
        'Bolivar', 'Pastaza', 'Tungurahua', 'Guayas', 'Santa Elena',
        'Los Rios', 'Azuay', 'Loja', 'El Oro', 'Esmeraldas', 'Manabi']
    )
    input_data["store_type"] = st.selectbox("Store Type", ['A', 'B', 'C', 'D', 'E'])
    input_data["cluster"] = st.slider("Cluster", 1, 17)

with col3:
    input_data["transactions"] = st.number_input("Transactions", 0, 10000)
    input_data["month"] = st.slider("Month", 1, 12)
    input_data["day"] = st.slider("Day", 1, 31)
    input_data["dayofweek"] = st.slider("Day of Week", 0, 6)

if st.button("Predict"):
    input_df = pd.DataFrame([input_data])

    # ✅ Group family into categories (match training)
    food_families = ['BEVERAGES', 'BREAD/BAKERY', 'DAIRY', 'DELI', 'EGGS', 'FROZEN FOODS',
                     'GROCERY I', 'GROCERY II', 'MEATS', 'POULTRY', 'PREPARED FOODS', 'PRODUCE', 'SEAFOOD', 'SNACK FOODS']
    home_families = ['HOME AND KITCHEN I', 'HOME AND KITCHEN II']
    clothing_families = ['LADIESWEAR', 'LINGERIE']
    grocery_families = ['SCHOOL AND OFFICE SUPPLIES', 'BOOKS']
    stationery_families = ['STATIONERY']
    cleaning_families = ['CLEANING', 'PERSONAL CARE']
    hardware_families = ['HARDWARE', 'PLAYERS AND ELECTRONICS']

    input_df["family"] = np.where(input_df["family"].isin(food_families), "FOODS", input_df["family"])
    input_df["family"] = np.where(input_df["family"].isin(home_families), "HOME", input_df["family"])
    input_df["family"] = np.where(input_df["family"].isin(clothing_families), "CLOTHING", input_df["family"])
    input_df["family"] = np.where(input_df["family"].isin(grocery_families), "GROCERY", input_df["family"])
    input_df["family"] = np.where(input_df["family"].isin(stationery_families), "STATIONERY", input_df["family"])
    input_df["family"] = np.where(input_df["family"].isin(cleaning_families), "CLEANING", input_df["family"])
    input_df["family"] = np.where(input_df["family"].isin(hardware_families), "HARDWARE", input_df["family"])

    # ✅ Apply preprocessing
    categorical_columns = ["family"]
    numerical_columns = ['store_nbr', 'onpromotion', 'cluster', 'transactions', 'month', 'day', 'dayofweek']

    input_df_cat = input_df[categorical_columns]
    input_df_num = input_df[num_imputer.feature_names_in_]

    st.write("num_imputer expects:", num_imputer.feature_names_in_)
    st.write("Input categorical columns:", input_df_cat.columns.tolist())
    st.write("Input numerical columns:", input_df_num.columns.tolist())

    input_df_cat_imputed = cat_imputer.transform(input_df_cat)
    input_df_num_imputed = num_imputer.transform(input_df_num)

    input_df_cat_encoded = pd.DataFrame(
        encoder.transform(input_df_cat_imputed),
        columns=encoder.get_feature_names_out(categorical_columns)
    )

    input_df_num_scaled = scaler.fit_transform(input_df_num_imputed)

    input_processed = np.hstack([input_df_num_scaled, input_df_cat_encoded.values])

    prediction = model.predict(input_processed)
    st.success(f"✅ Predicted Sales: {prediction[0]:,.2f}")

    st.write("cat_imputer expects:", cat_imputer.feature_names_in_)

