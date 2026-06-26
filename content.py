import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.set_page_config(
    page_title="Content Monetization Modeler",
    layout="wide",
    
)

st.markdown("""
<style>

.stApp {
    background-color: #0A192F;
}

[data-testid="stSidebar"] {
    background-color: #1c1c24;
}

h1, h2, h3, h4 {
    color: white !important;
    font-weight: bold !important;
}

label {
    color: red !important;
    font-weight: 600 !important;
}

input {
    color: white !important;
}
.stNumberInput input {
     background-color: #B3E5FC !important;
    color: #000000 !important;
    font-weight: bold !important;
            }
.stSelectbox div[data-baseweb="select"] {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

st.title(" Predict YouTube Ad Revenue")

MODEL_PATH = 'C:/Users/Welcome/linear_regression_model.pkl'

if not os.path.exists(MODEL_PATH):
    st.error(" Model file not found. Please check the path.")
    st.stop()

model = joblib.load(MODEL_PATH)
print("Intercept:")
print(model.intercept_)

print("\nCoefficients:")
coef_df = pd.DataFrame({
    "Feature": model.feature_names_in_,
    "Coefficient": model.coef_
})

print(coef_df)


feature_cols = [
    
    'views',
    'likes',
    'comments',
    'watch_time_minutes',
    'video_length_minutes',
    'subscribers',
    'year',
    'month',
    'day',
    
]
print(type(model))
print(feature_cols)
st.subheader(" Enter Video Feature Values")

input_data = {}
cols_per_row  = 3
rows = (len(feature_cols) + cols_per_row - 1) // cols_per_row

for i in range(rows):
    cols = st.columns(cols_per_row)
    for j in range(cols_per_row):
        idx = i * cols_per_row + j
        if idx < len(feature_cols):
            col_name = feature_cols[idx]
            #input_data[col_name] = cols[j].number_input(f"{col_name}", value=0.0)
            if col_name == "year":
                input_data[col_name] = cols[j].number_input(
                    "Year",
                    min_value=2000,
                    max_value=2030,
                    value=2024,
                    step=1
                )

            elif col_name ==        "month":
                input_data[col_name] = cols[j].number_input(
                    "Month",
                    min_value=1,
                    max_value=12,
                    value=1,
                    step=1
                )

            elif col_name == "day":
                input_data[col_name] = cols[j].number_input(
                    "Day",
                    min_value=1,
                    max_value=31,
                    value=1,
                    step=1
                )

            else:
                input_data[col_name] = cols[j].number_input(
                    f"{col_name}",
                    value=0.0
                )
st.subheader("Categorical Features")

category = st.selectbox(
    "Category",
    [ "Entertainment", "Gaming", "Lifestyle", "Music", "Tech"]
)

device = st.selectbox(
    "Device",
    [ "Mobile", "TV", "Tablet"]
)

country = st.selectbox(
    "Country",
    [ "CA", "DE", "IN", "UK", "US"]
)

day_of_week = st.selectbox(
    "Day of Week",
    [0, 1, 2, 3, 4, 5, 6]
)


if st.button("Predict"):

    try:
        
        input_data['engagement_rate'] = (
            input_data['likes'] + input_data['comments']
        ) / max(input_data['views'], 1)

        
        input_df = pd.DataFrame([input_data])

        
        input_df["category_Entertainment"] = int(category == "Entertainment")
        input_df["category_Gaming"] = int(category == "Gaming")
        input_df["category_Lifestyle"] = int(category == "Lifestyle")
        input_df["category_Music"] = int(category == "Music")
        input_df["category_Tech"] = int(category == "Tech")

        
        input_df["device_Mobile"] = int(device == "Mobile")
        input_df["device_TV"] = int(device == "TV")
        input_df["device_Tablet"] = int(device == "Tablet")

        
        input_df["country_CA"] = int(country == "CA")
        input_df["country_DE"] = int(country == "DE")
        input_df["country_IN"] = int(country == "IN")
        input_df["country_UK"] = int(country == "UK")
        input_df["country_US"] = int(country == "US")

        
        for i in range(1, 7):
            input_df[f"day_of_week_{i}"] = int(day_of_week == i)

        input_df = input_df[[
                'views',
                'likes',
                'comments',
                'watch_time_minutes',
                'video_length_minutes',
                'subscribers',
                'year',
                'month',
                'day',
                'category_Entertainment',
                'category_Gaming',
                'category_Lifestyle',
                'category_Music',
                'category_Tech',
                'device_Mobile',
                'device_TV',
                'device_Tablet',
                'country_CA',
                'country_DE',
                'country_IN',
                'country_UK',
                'country_US',
                'day_of_week_1',
                'day_of_week_2',
                'day_of_week_3',
                'day_of_week_4',
                'day_of_week_5',
                'day_of_week_6',
                'engagement_rate'
            ]]
        print(input_df)


           

        prediction = model.predict(input_df)[0]
        prediction = max(0, prediction)

        st.success(
            f" Predicted Ad Revenue: ${prediction:,.2f}"
        )

        if prediction == 0:
            st.info(
                "This video may not generate ad revenue based on the current input values."


            )

        if prediction < 500:
            st.info("Low revenue potential. Consider improving engagement and watch time.")
        elif prediction < 1500:
            st.info(" Moderate revenue potential. The video is performing reasonably well.")
        else:
            st.info(" High revenue potential! Strong engagement and watch time are driving revenue growth.")

    except Exception as e:
               st.error(f"Prediction error: {str(e)}")

