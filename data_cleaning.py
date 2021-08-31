# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:24:50 2021

@author: Seong
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')







#salary parsing
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)
df = df[df['Salary Estimate'] != '-1']
Salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = Salary.apply(lambda x: x.replace('K', '').replace('$',''))

minus_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:', ''))

df['min_salary'] = minus_hr.apply(lambda x: int(x.split('-')[0]) if '-' in x else x)
df['max_salary'] = minus_hr.apply(lambda x: int(x.split('-')[1]) if '-' in x else x)
df['average_salary'] = (df.min_salary.astype(int) + df.max_salary.astype(int))/2

#Removing "-1" Ratings
df = df[df['Rating'] != -1]


#state field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1] if ',' in x else x)

#Clean up "Founded" and calculate age of the company
df['company_age'] = df.Founded.apply(lambda x: 0 if x <1 else 2021 - x)

#Parsing job description
df['Job Description'][0]

#python
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

#R studio
df['R studio'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)

#SQL
df['SQL'] = df['Job Description'].apply(lambda x: 1 if 'SQL' in x.lower() else 0)

#Power BI
df['Power BI'] = df['Job Description'].apply(lambda x: 1 if 'Power BI' in x.lower() else 0)

#excel
df['Excel'] = df['Job Description'].apply(lambda x: 1 if 'Excel' in x.lower() else 0)

df.to_csv('salary_data_cleaned.csv')
