
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
 * Grasp the effects of perosnal and geographical aspects on the payment for helathcare insrnace 
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

## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).
* How were data insights communicated to technical and non-technical audiences?
* Explain how the dashboard was designed to communicate complex data insights to different audiences. 

## Unfixed Bugs
* Please mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation are not valid reasons to leave bugs unfixed.
* Did you recognise gaps in your knowledge, and how did you address them?
* If applicable, include evidence of feedback received (from peers or instructors) and how it improved your approach or understanding.

## Development Roadmap
* What challenges did you face, and what strategies were used to overcome these challenges?
* What new skills or tools do you plan to learn next based on your project experience? 

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. From the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Thank the people who provided support through this project.
