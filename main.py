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