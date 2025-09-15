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

# C. Basic Visual
# Bar graph of schools by type
school_by_type = df['school_type'].value_counts()
plt.figure(figsize=(8,5))
school_by_type.plot(kind="bar",color="green")
plt.title("Bar graph of school by type")
plt.xlabel("School Type")
plt.xticks(rotation=55)
plt.ylabel("Number of School")
for i,values in enumerate(school_by_type):
    plt.text(i,values+(0.01*values),str(values),ha="center",fontsize=8)
plt.show()

# Histogram of funding_per_student_usd
data = df['funding_per_student_usd']
counts, bins, _ = plt.hist(data, bins='auto', color='green', edgecolor='black')
for i in range(len(counts)):
    plt.text(bins[i] + (bins[i+1]-bins[i])/2, counts[i], int(counts[i]),
             ha='center', va='bottom')

plt.title("Histogram of Funding per Student")
plt.xlabel("Funding per Student (USD)")
plt.ylabel("Number of Schools")
plt.show()

# Histogram of avg_test_score_percent
data = df['avg_test_score_percent']
counts, bins, _= plt.hist(data,bins='auto',color='green',edgecolor='black')
for i in range(len(counts)):
    plt.text(bins[i] + (bins[i+1]-bins[i])/2, counts[i], int(counts[i]),ha='center', va='bottom')

plt.title("Histogram of Average test score percent")
plt.xlabel("Average Test Score (%)")
plt.ylabel("Number of Schools")
plt.show()