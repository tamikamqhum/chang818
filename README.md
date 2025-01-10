
# Project CareLens

**Project CareLens** is a project that applies visualisation techniques to analyse health related data and extract trends.

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


## Dataset Content
A dataset that is not overly large has been crated for consideration (approximately 1300 rows and 7 columns). Basic information regarding healthcare and how varibales such as perosnal characteristics and geographical location affect these expenses is inlcuded in the dataset. Key Columns include: 
* Age: Age of the insured 
* Gender: Gender of the insured (male or female)
* BMI: Body Mass Index indicating body fat 
* Children: Number of dependents 
* Smoker: Whether person smokes or not (yes or no)
* Region: Area where the insured is 
* Charges: Expenses that are incurred by healthcare insurance 


## Business Requirements
Objectives:
 * Grasp the effects of perosnal and geographical aspects on the payment for healthcare insurance
 * Formulate managing models that aid in healthcare expense prediction 

 Requirements:  
 * Examine how age, gender, BMI, smoking, family size and the region affect the cost 
 * Provide visual aids that showcase trend patterns 
 * Formulate models that reflect the expected cost of insurnace in relation to personal traits 


## Hypothesis and Validation 
Hypothesis: 
1. The smoking status distinctly affects the amount charged for a healthcare insurance 
2. There are regional differences in the amount of the payment for healthcare services, some of which have higher payments 
3. Healthcare insurance costs can be reliably forcasted using Age and BMI as variables 

Validation: 
* Use regression models to test predictions for healthcare charges based on these factors


## Project Plan
Steps: 
1. Data Collection: 
   * The dataset can be obtained from a CSV file from kaggle https://www.kaggle.com/datasets/willianoliveiragibin/healthcare-insurance/data 

2. Data Processing: 
   * Remove outliers and clean data by taking care of missing data 
   * Encode the relevent features including 'gender', 'smoker'and 'region' 
   * Create more features such as BMI categories and age groups

3. Data Analysis 
   * Conduct descriptive statistics to analyse important metrics such as average charges by gender, region, etc...
   
4. Predictive Modeling: 
   * Use the key features to develop models that can accurately predict healthcare costs 

5. Visualisation:
   * Include visual representation for correlations, trends and how different features affcet the charges 

## Business Requirements and Visualisation Rationale
Business Requirements: 
 1. Impact of Region: Visualise charges across regions 
 2. Effect of Smoking: Show how smoking increases healthcare costs 
 3. Predictive Analysis: Visualise how predictions are made for healthcare charges

Rationale: 
Every business will be represented by the visual equivalent: 
 1. Impact of Region: Heatmap or Bar chart showing average charges by region
 2. Effect of Smoking: Box Plot or bar chart of comparison between smoking and non-smoking insurnace cost 
 3. Predictive Analysis: Scatter plot indicating the accuracy of the prediction 

## Analysis Techniques Used
Methods:
 1. Descriptive Analysis: Mean, median, and variance of charges depending on each attribute (age, gender, region)
 2. Correlation Analysis: Pearson correlation to find relationships between features and charges.
 3. Regression Model:Linear regression and decision trees to predict charges 

Limitation: 
 * Small sample size may restrict the capacity of prediction generalisation 
 * Data quality problems,e.g., missing values, may have an impact when tackling model accuracies 

Alternative Approaches: 
 * Employ more sophifiscated models 

Generative AI Tools: 
 * AI tools helped exploit opportunities in code optimisation and visualising concept 


## Ethical considerations
 * Data Privacy: Nonsensitive personal data is not present in the dataset but ethical considerations were taken into account regarding the anonymizing of any ground-truth data
 * Bias and Fairness: Made sure that the analysis did not discriminate among genders or regions in favour of any. Bias was avoided by providing an equal respresentation of all the categories in the dataset

Legal/Societal issues: 
 * The dataset was obtained from Kaggle, therefore properly anonymised and handled 

## Conclusion
In conclusion, this project revealed several important insights about healthcare costs. Smokers incur significantly higher healthcare expenses compared to non-smokers, largely due to smoking-related health issues such as cardiovascular diseases, respiratory conditions, and cancer. Reducing smoking rates through various programmes could substantially lower healthcare costs for individuals and insurers alike.

Regional differences in healthcare costs are evident, with regions like the Northeast experiencing higher charges compared to the Southwest. These variations may be influenced by factors such as healthcare access, income levels, and differing health risk profiles. Addressing these disparities requires a closer look at regional healthcare policies and demographics, with a focus on allocating resources to high-cost regions.

The analysis also showed that healthcare costs increase with age and BMI. Older individuals and those with higher BMI values face higher healthcare expenses due to age-related health issues and conditions such as diabetes and hypertension. Promoting preventive care and wellness programmes targeted at these populations could help reduce long-term healthcare costs.

Lastly, the impact of children and gender on healthcare costs was found to be minimal. The number of children in a family and gender do not significantly affect individual healthcare expenses compared to factors like smoking, region, age, and BMI.

Overall, the visualisations, including heatmaps, boxplots, and scatter plots, effectively highlighted these findings and provided a clear understanding of the factors influencing healthcare costs. These insights can inform policies and initiatives aimed at managing and reducing healthcare expenses.

## Development Roadmap/ Unfixed Bugs
Throughout this project, I faced several challenges. Understanding and cleaning the dataset was a significant hurdle, particularly when dealing with missing data and errors such as KeyError. Transforming data into meaningful features, like creating BMI categories and age groups, required careful consideration. Selecting appropriate visualisations to gain insights and predicting healthcare costs while evaluating models effectively also presented challenges. To tackle these issues, I adopted an incremental problem-solving approach, breaking down problems step-by-step. I leveraged powerful tools like Pandas, Seaborn, and Scikit-learn, continuously refining my processes for better accuracy and clarity. Along the way, I engaged in ongoing research and learning to address unfamiliar challenges.

During this journey, I acquired several new skills and learned how to use various tools. I became proficient in data manipulation using Pandas, mastering techniques like groupby and apply. I also learned how to create effective visualisations with Seaborn and Matplotlib. I improved my debugging and error-handling skills to ensure smoother workflows.

Looking ahead, I plan to explore advanced machine learning models and further delve into feature engineering. I aim to automate my analysis workflows by creating reusable code and to experiment with interactive visualisations using tools like Plotly. Finally, I intend to handle larger datasets by utilising scalable tools. These future plans will help me build on the knowledge and skills I have gained during this project and continue to develop my expertise in data analysis and visualisation.

## Main Data Analysis Libraries
* Pandas - Data Manipulation and Analysis (e.g. Loading the dataset and Descriptive statistics)
* Seaborn - Data Visualisation (e.g. Boxplot and Heatmap)
* Matplotlib - Plotting and visualisation used alongside Seaborn (e.g. Scatter plot for predictions)

## Credits 

1. With a little help from OpenAI's ChatGPT, the Python code for this project’s data visualizations—featuring heatmaps, box plots, and scatter plots—came to life. The project taps into widely-used libraries like pandas, seaborn, and matplotlib to break down and illustrate healthcare insurance data effectively.
2. Code Institute - LMS https://learn.codeinstitute.net/ci_program/daai_2 for indepth explanation for things i did not understand
3. https://github.com/adam-p/markdown-here/wiki/markdown-cheatsheet To structure my Notebook 


## Acknowledgements (optional)
* Thank you to Vasi Pavaloi and Neil McEwen for their guidance and pateince throughout the Hackathon
