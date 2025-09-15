import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("education_inequality_data.csv")

# Level 1: Understanding & Cleaning the Data
# A. Data Quality Check
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum()) # check missing value
print(df.duplicated().sum()) # check duplicated sum

# B. Basic Summaries
# Number of schools by state,school type and grade level
school_by_state = df['state'].value_counts() # for state
print(school_by_state)

school_by_type = df['school_type'].value_counts() # for type
print(school_by_type)

school_by_level = df['grade_level'].value_counts() # for grade level
print(school_by_level)