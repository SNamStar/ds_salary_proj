# Data Science Salary Estimator: Project Overview
- Created a tool that estimates data science salaries to help them negotiate their income when getting their job
- Scraped around 250 job descriptions from glassdoor using python and selenium. The jobs were all located in the US
- Engineered features from text of each job descriptions to quantify the value companies put on Python, R Studio, SQL, Power BI, and excel
- Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model
- Built a client facing API using flask

## Codes and Resources ##
**Python Version:** 3.7

**Packages:** pandas, numpy, sklearn, matplotlib,seaborn, selenium, flask, json, pickle

**For Web Framework Requirements:** `pip install -r requirements.txt`

**Scraper Article**: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905

*It should be noted the scraper code in the article was incompatible with the current version of glassdoor website. The scraper blow was used instead to achieve desired database*

**Scraper github**: https://github.com/wizrox/dsSlryProj/blob/master/glassdoor_scrapper.py
**Markdown guide for this Readme**: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

# Youtube Project walkthrough:
I followed youtuber Ken Jee's multi-part videos for this project
https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t

# Web Scraping
Tweaked the scraper github repo from oabove to scrape 250 job postings from glassdoor.com. There was a continued server error if trying to go above. With each job, the following information were obtained:
- Job title
- Salary Estimate
- Job Description
- Rating
- Company Name
- Company Size
- Company Founded Date
- Type of Industry
- Revenue

# Data Cleaning
After scraping the data, some cleaning was needed to make it usable for the model. The following changes and additions were made:
- Parsed numeric data out of salary
- Made columns for employer provided salary and hourly wages
- Removed rows without salary
- Made a new column for company state
- Transformed founded date into age of the company
- Made columsn for if different skills were listed in the job description:
  - Python
  - R Studio
  - SQL
  - Power BI
  - Excel
 - Column for simplified job title and Seniority
 
# EDA
I looked at the distributions of the data and the value counts for the various caregorial variables. Below are a few highlights from the pivot tables

![pivottable](https://user-images.githubusercontent.com/77301106/134084045-8c3b3d0f-380f-4230-98c0-9a3c7e319e47.PNG)
![heatmap](https://user-images.githubusercontent.com/77301106/134083808-d59cbd97-c995-4aaf-b2b1-a8dd86e3aae2.PNG)
![industry type](https://user-images.githubusercontent.com/77301106/134083866-7e1c980c-26bd-43d1-a529-f83a45ce33f5.PNG)

# Model Building
First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%

I treid three different models and evaluated them using Mean Absolute Error. This was because it was easy to interpret and outlies aren't particularly bad in for this type of model:
  - **Multiple Linear Regression:** Baseline for the model.
  - **Lasso Regression:** Because of the sparse data from the many categorial variables, I thought a normalized regression like this would be effective.
  - **Random Forest:** Same reason as for using Lasso Regression
  
# Model performance
The results from these are:
  - **Linear Regression MAE:** 24.20
  - **Lasso Regression MAE:** 14.91
  - **Random Forest MAE:** 14.67
So the Random Forest model outperformed other approaches

# Productionization
Finally, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.

