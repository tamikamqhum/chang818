import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import numpy as np

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


# Function for predictive modelling
def estimate_insurance_cost(age, bmi, region, smoker_status):
    region_map = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}
    smoker_map = {"yes": 1, "no": 0}
    
    # Train a simple model
    X = df[['age', 'bmi', 'region_code', 'smoker_code']]
    y = df['charges']
    
    model = LinearRegression()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    
    input_data = np.array([age, bmi, region_map.get(region, 0), smoker_map.get(smoker_status, 0)]).reshape(1, -1)
    predicted_cost = model.predict(input_data)
    return predicted_cost[0]

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

# Visual Analysis Section
def visual_analysis():
    st.title("Visual Analysis 📊")
    
    # Plotting relationships
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df, x="age", y="charges", hue="smoker", palette="coolwarm", ax=ax)
    ax.set_title("Age vs Insurance Charges (Smoker vs Non-Smoker)")
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x="region", y="charges", ax=ax, palette="Set3")
    ax.set_title("Insurance Charges by Region")
    st.pyplot(fig)

# Predictive Modelling Section
def predictive_modelling():
    st.title("Predictive Modelling 🔮")
    st.write("Estimate the insurance cost based on inputs below.")
    
    age_input = st.number_input("Enter your age:", min_value=18, max_value=100, value=30)
    bmi_input = st.number_input("Enter your BMI:", min_value=10.0, max_value=50.0, value=25.0)
    region_input = st.selectbox("Select your region:", df["region"].unique())
    smoker_input = st.selectbox("Do you smoke?", ["yes", "no"])
    
    if st.button("Estimate Cost"):
        predicted_cost = estimate_insurance_cost(age_input, bmi_input, region_input, smoker_input)
        st.write(f"Estimated Insurance Cost: ${predicted_cost:.2f}")

# Download Reports Section
def download_reports():
    st.title("Download Reports 📥")
    
    report_format = st.selectbox("Select Report Format", ["CSV", "PDF"])
    
    if report_format == "CSV":
        csv = df.to_csv(index=False)
        st.download_button(label="Download CSV", data=csv, file_name="insurance_data.csv", mime="text/csv")
    
    elif report_format == "PDF":
        # You could use a PDF generation library like FPDF to generate a custom PDF report
        # For simplicity, this is just a placeholder for now.
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
        visual_analysis()
    elif selection == "Predictive Modelling":
        predictive_modelling()
    elif selection == "Download Reports":
        download_reports()

if __name__ == "__main__":
    main()
