# Project CareLens - Advanced Version  

**Project CareLens** applies data analysis, machine learning, and visualisation techniques to uncover trends in healthcare insurance expenses. This enhanced version builds upon the original by refining the dataset, improving visualisations, implementing advanced ML models, and deploying an interactive Streamlit app.

# ![Health Insurance ](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlqlzrBQ6v_rq-kPdooJPeqmMYjFucyq8Ylw&s)

## Dataset Content
The dataset consists of ~1300 rows and 7 columns:
* **AGE:** Insured person's age  
* **GENDER:** Male/Female  
* **BMI:** Body Mass Index (indicator of body fat)  
* **CHILDREN:** Number of dependants  
* **SMOKER:** Smoking Status (Yes/No)  
* **REGION:** Residential area of the insured  
* **CHARGES:** Medical insurance cost  

# Enhancements  
**Data Cleaning:**  
   - Removing outliers  
   - Handling missing values  
   - Encoding categorical variables  

**Feature Engineering:**  
   - Creating:  
      - BMI categories  
      - Age groups  
   - Interaction terms for better predictions  

## Business Objectives  
1. **Impact of Demographics on Healthcare Costs** - Understand how personal and geographical characteristics affect expenses.
2. **Predictive Modelling** - Build ML models to forecast insurance charges  
3. **Data-driven Insights** - Create actionable insights for policymakers and insurance companies  

## Hypothesis and Validation  
| Hypothesis | Validation Method |
|------------|------------------|
| Smokers have significantly higher insurance costs. | Regression models, statistical analysis |
| Certain regions exhibit higher insurance expenses than others. | Correlation analysis, real-world comparison |
| Age and BMI are strong predictors of healthcare costs. | Train-test validation, model evaluation |

## Project Plan  
1. **Data Processing**  
   - Clean dataset (remove duplicates, handle missing values)  
   - Encode categorical features  
   - Feature engineering (BMI classification, age segmentation)  

2. **Exploratory Data Analysis (EDA)**  
   - Descriptive statistics  
   - Correlation analysis  
   - Advanced visualisations: heatmaps, box plots, scatter plots  

3. **Machine Learning Models**  
   - Linear Regression  
   - Decision Trees & Random Forests  
   - Gradient Boosting Models (XGBoost, LightGBM)  
   - Model evaluation with RMSE, MAE, and R2 score  

4. **Interactive Web App**  
   - Built using **Streamlit** for real-time exploration  
   - Features: cost prediction, comparison charts, insights  

## Business Requirements and Visualisation Rationale  
| Requirement | Visualisation |
|------------|--------------|
| **Impact of Region** | Heatmap of average insurance charges per region. |
| **Effect of Smoking** | Box plot comparing smokers vs. non-smokers. |
| **Age vs. Charges** | Scatter plot showcasing trends in age and healthcare costs. |
| **BMI vs. Charges** | Regression plots indicating BMI impact. |

## Main Data Analysis Libraries  
| Library | Purpose |
|---------|---------|
| **Pandas** | Data manipulation and preprocessing |
| **NumPy** | Numerical computations |
| **Matplotlib & Seaborn** | Data visualisation |
| **Scikit-learn** | Machine learning modelling |
| **Streamlit** | Web application framework |

## Deployment Roadmap  
**Streamlit App:** Deploy interactive dashboard with real-time predictions  

## Dashboard Design  
- **Homepage** – Overview of insurance trends, key insights.  
- **Data Exploration** – Filters for age, BMI, region, smoker status.  
- **Visual Analysis** – Charts and graphs to showcase relationships.  
- **Predictive Modelling** – User input for insurance cost estimation.  
- **Download Reports** – Export analysis as PDF/CSV.  

## Ethical Considerations  
- **Data privacy**: No sensitive personal data is used.  
- **Bias prevention**: Ensuring fair representation across all demographic factors.  
- **Legal/Societal issues:** The dataset was obtained from Kaggle, therefore properly anonymised and handled.  

## Limitations  
- **Sample Size**: Limited dataset may not generalise to wider populations.  
- **Feature Bias**: Dataset may have unaccounted confounding variables.  
- **Model Accuracy**: Simpler models may not capture complex healthcare cost drivers.  

## Unfixed Bugs  
- Some missing values require further investigation.  
- Model accuracy can be improved with additional feature engineering.  
- Streamlit app UI enhancements for better user experience.  

## Future Improvements  
- Deploy a REST API for real-time insurance cost predictions.  
- Explore deep learning models for better forecasting.  
- Incorporate additional datasets for broader insights.  

## Conclusion  
This project provides valuable insights into healthcare insurance expenses, demonstrating how personal attributes like age, BMI, and smoking status significantly impact costs. The analysis highlights regional disparities and offers predictive capabilities to estimate future healthcare expenses. By leveraging machine learning models and data visualisation, CareLens offers an evidence-based approach to understanding and managing insurance pricing strategies.  

## Credits  
1. OpenAI's ChatGPT for helping with code optimisation and structuring.  
2. Code Institute for explanations and tutorials on data scientist and researchers who provided valuable insights and feedback throughout this project.  