import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Level 2: Intermediate (Exploring Relationships)
# D. Find patterns & correlations 
numeric_df = df.select_dtypes(include=['float64', 'int64'])
corr = numeric_df.corr()
print(corr)
plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Correlation Heatmap of School Factors")
plt.show()

# E. Group Comparisons (categorical vs numeric)
avg_scores_by_type = df.groupby("school_type")["avg_test_score_percent"].mean()
print(avg_scores_by_type)
plt.figure(figsize=(8,5))
avg_scores_by_type.plot(kind="bar", color="green", edgecolor="black")
plt.title("Average Test Scores by School Type")
plt.xlabel("School Type")
plt.ylabel("Average Test Score (%)")
plt.xticks(rotation=0)
for i, value in enumerate(avg_scores_by_type):
    plt.text(i, value + 0.5, f"{value:.1f}", ha="center", fontsize=9)
plt.show()

# F. Scatter Plots 
# Funding vs Test Score
plt.figure(figsize=(7,5))
sns.regplot(x="funding_per_student_usd", y="avg_test_score_percent", data=df,
            scatter_kws={"alpha":0.6, "color":"blue"}, line_kws={"color":"red"})
plt.title("Funding vs Test Scores (with Trend Line)")
plt.xlabel("Funding per Student (USD)")
plt.ylabel("Average Test Score (%)")
plt.show()

# Student-Teacher Ratio vs Test Score
plt.figure(figsize=(7,5))
sns.regplot(x="student_teacher_ratio", y="avg_test_score_percent", data=df,
            scatter_kws={"alpha":0.6, "color":"blue"}, line_kws={"color":"red"})
plt.title("Student-Teacher Ratio vs Test Score")
plt.xlabel("Student Teacher Ratio")
plt.ylabel("Test Score")
plt.show()

# Scatter Plots || Percent Low-Income vs Dropout Rate
plt.figure(figsize=(7,5))
sns.regplot(x="percent_low_income", y="dropout_rate_percent", data=df,
            scatter_kws={"alpha":0.6, "color":"blue"}, line_kws={"color":"red"})
plt.title("Percent Low-Income vs Dropout Rate")
plt.xlabel("percent_low_income")
plt.ylabel("dropout_rate_percent")
plt.show()