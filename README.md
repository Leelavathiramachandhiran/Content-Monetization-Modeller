# CONTENT MONETIZATION MODELLER


A machine learning project that predicts YouTube ad revenue based on video performance metrics and contextual features. This project implements multiple regression models and provides an interactive Streamlit web application for revenue predictions.

# TECHOLOGGY USED

- Python 3.x
- Machine Learning: Scikit-learn
- Data Analysis: Pandas, NumPy
- Visualization: Matplotlib, Seaborn
- Web App: Streamlit
- Model Persistence: Joblib, Pickle

# DATASET INFORMATION

- Name: YouTube Monetization Modeler Dataset
- Format: CSV
- Size: ~122,000 rows
- Target Variable: `ad_revenue_usd`

# METTHODOLOGY
   1. Data Preprocessing
   2. Exploratory Data Analysis
   3. Model Building & Evaluation
   4. Model Selection
   5. Streamlit App Development

# KEY INSIGHTS:
   1. Strong Predictive Power: All models achieved >95% R² score, indicating excellent predictive capability
   2. Feature Importance: Views, engagement metrics, and subscriber count are primary revenue drivers
   3. Model Consistency: Linear models (Linear, Ridge, Lasso) performed similarly, suggesting linear relationships
   4. Engagement Rate: The engineered feature significantly improved model interpretability
