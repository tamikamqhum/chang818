import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import numpy as np
import plotly.express as px

# Set the custom theme
primaryColor="#3498db"
backgroundColor="#f8f9fa"
secondaryBackgroundColor="#66b5b5"
textColor="#0e0e0e"

st.set_page_config(page_title="CareLens Dashboard", page_icon="🏥", layout="wide")

# Custom CSS to style the page
st.markdown(f"""
    <style>
        .main {{
            background-color: {backgroundColor};
        }}
        .block-container {{
            background-color: {secondaryBackgroundColor};
        }}
        h1, h2, h3 {{
            color: {textColor};
        }}
        .stButton {{
            background-color: {primaryColor};
            color: white;
        }}
        .stTextInput {{
            background-color: {secondaryBackgroundColor};
        }}
    </style>
""", unsafe_allow_html=True)

# Load Dataset
df = pd.read_csv("C:\\Users\\tmqhu\\Documents\\chang818\\health_insurance.csv")

# Data Preprocessing: Add region_code and smoker_code
df['region_code'] = df['region'].map({'southeast': 0, 'southwest': 1, 'northeast': 2, 'northwest': 3})
df['smoker_code'] = df['smoker'].map({'yes': 1, 'no': 0})

# Function for predictive modelling
def estimate_insurance_cost(age, bmi, region, smoker_status, model):
    region_map = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}
    smoker_map = {"yes": 1, "no": 0}
    
    # Prepare input data for prediction
    input_data = pd.DataFrame({
        'age': [age],
        'bmi': [bmi],
        'region_code': [region_map.get(region, 0)],
        'smoker_code': [smoker_map.get(smoker_status, 0)]
    })
    
    predicted_cost = model.predict(input_data)
    return predicted_cost[0]

# Model Evaluation Function
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mse = mean_absolute_error(y_test, y_pred)
    return mse

# Interactive Visualization using Plotly
def interactive_visualization():
    st.title("Interactive Visualization 📊")
    fig = px.scatter(df, x="age", y="charges", color="smoker", hover_data=["region", "bmi"], title="Age vs Insurance Charges")
    st.plotly_chart(fig)

# Predictive Modelling Section
def predictive_modelling():
    st.title("Predictive Modelling 🔮")
    st.write("Estimate the insurance cost based on inputs below.")

    # Model Selection
    model_type = st.radio("Choose a model", ["Linear Regression", "Ridge", "Lasso", "Random Forest"])

    # Train the selected model
    X = df[['age', 'bmi', 'region_code', 'smoker_code']]
    y = df['charges']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    if model_type == "Linear Regression":
        model = LinearRegression()
    elif model_type == "Ridge":
        model = Ridge()
    elif model_type == "Lasso":
        model = Lasso()
    else:
        model = RandomForestRegressor()

    model.fit(X_train, y_train)
    
    # Display model evaluation metrics
    mse = evaluate_model(model, X_test, y_test)
    st.write(f"Mean Squared Error: {mse:.2f}")
    
    # User Inputs for Prediction
    age_input = st.number_input("Enter Age", min_value=18, max_value=100, value=25)
    bmi_input = st.number_input("Enter BMI", min_value=10, max_value=50, value=25.0)
    region_input = st.selectbox("Select Region", ["northeast", "northwest", "southeast", "southwest"])
    smoker_input = st.selectbox("Smoker Status", ["yes", "no"])

    # Predict Insurance Cost
    predicted_cost = estimate_insurance_cost(age_input, bmi_input, region_input, smoker_input, model)
    st.write(f"Predicted Insurance Cost: ${predicted_cost:.2f}")

    # Display Prediction Breakdown
    region_map = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}
    smoker_map = {"yes": 1, "no": 0}

    age_contribution = model.coef_[0] * age_input
    bmi_contribution = model.coef_[1] * bmi_input
    region_contribution = model.coef_[2] * region_map.get(region_input, 0)
    smoker_contribution = model.coef_[3] * smoker_map.get(smoker_input, 0)
    
    total_contribution = age_contribution + bmi_contribution + region_contribution + smoker_contribution
    
    st.write(f"### Prediction Breakdown")
    st.write(f"- Age Contribution: {age_contribution:.2f}")
    st.write(f"- BMI Contribution: {bmi_contribution:.2f}")
    st.write(f"- Region Contribution: {region_contribution:.2f}")
    st.write(f"- Smoker Contribution: {smoker_contribution:.2f}")
    st.write(f"- **Total Predicted Insurance Cost: ${total_contribution:.2f}**")

# Homepage section
def homepage():
    st.title("Welcome to the CareLens Insurance Dashboard 🚑")
    st.write("""
    ## Overview of Insurance Trends
    - The insurance costs are largely impacted by factors such as age, BMI, smoking status, and region.
    - Our analysis reveals that smokers tend to pay significantly higher premiums.
    - Geographically, residents in the Southeast region tend to have higher premiums.
    """)
    st.image("insurance_trends.jpg", caption="Insurance Trends Visualization")

# Data Exploration Section
def data_exploration():
    st.title("Data Exploration 🔍")
    
    # Sidebar filters
    age_filter = st.slider("Age", int(df["age"].min()), int(df["age"].max()), (int(df["age"].min()), int(df["age"].max())))
    bmi_filter = st.slider("BMI", float(df["bmi"].min()), float(df["bmi"].max()), (float(df["bmi"].min()), float(df["bmi"].max())))
    region_filter = st.selectbox("Region", df["region"].unique())
    smoker_filter = st.selectbox("Smoker Status", ["yes", "no"])
    
    filtered_data = df[(df['age'] >= age_filter[0]) & (df['age'] <= age_filter[1]) & 
                       (df['bmi'] >= bmi_filter[0]) & (df['bmi'] <= bmi_filter[1]) & 
                       (df['region'] == region_filter) & (df['smoker'] == smoker_filter)]
    
    st.write(filtered_data)

# Download Reports Section
def download_reports():
    st.title("Download Reports 📥")
    
    report_format = st.selectbox("Select Report Format", ["CSV", "PDF"])
    
    if report_format == "CSV":
        csv = df.to_csv(index=False)
        st.download_button(label="Download CSV", data=csv, file_name="insurance_data.csv", mime="text/csv")
    
    elif report_format == "PDF":
        st.write("PDF report generation coming soon!")

# Main app routing
def main():
    st.sidebar.title("CareLens Dashboard Menu")
    selection = st.sidebar.radio("Go to", ["Homepage", "Data Exploration", "Visual Analysis", "Predictive Modelling", "Download Reports"])
    
    if selection == "Homepage":
        homepage()
    elif selection == "Data Exploration":
        data_exploration()
    elif selection == "Visual Analysis":
        interactive_visualization()
    elif selection == "Predictive Modelling":
        predictive_modelling()
    elif selection == "Download Reports":
        download_reports()

if __name__ == "__main__":
    main()
