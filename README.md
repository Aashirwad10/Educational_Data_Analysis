## Data Source

The dataset used in this project is from [Kaggle: Education Inequality Data](https://www.kaggle.com/datasets/shamimhasan8/education-inequality-data)  
License: [MIT License](https://opensource.org/licenses/MIT)  
Original author: Shamim Hasan

---
## A. Data Quality Check
### Preview (Screenshot)
![Data Head](images/head.png)
- 🔼 *It gives us a look into our 1st 5 row*
- `df.head()`

![Data info](images/info.png)
- 🔼 *shows all column, data types, missing values....*
- `df.info()`

![Describe](images/describe.png)
- 🔼 *It gives min,max,mean....*
- `df.describe()`

![Checking Missing values](images/missingvalue.png)
- 🔼 *Checks if we have any missing values*
- `df.isnull().sum()`

![Checking duplicate values](images/duplicate.png)
- 🔼 *Checks if we have any duplicates*
- `df.duplicated().sum()`
---

## B. Basic Summaries
### Preview (Screenshot)

![School by state](images/school_by_state.png)
- 🔼 *It gives us info on how many schools are there in states*
- `school_by_state`

![School by type](images/school_by_type.png)
- 🔼 *It gives us info on school type*
- `school_by_type`

![School by level](images/school_by_level.png)
- 🔼 *It gives us info on level of school*
- `school_by_level`
---

## C. Basic Visual
### Preview (Screenshot)
![Bar graph of schools by type](images/school_by_type_plot.png)
- 🔼 *Bar Graph on schools by type*
- `school_by_type`

![Histogram of funding_per_student_usd](images/funding_per_student_usd_plot.png)
- 🔼 *Histogram of funding per student (in usd)*
- `funding_per_student_usd`

![Histogram of avg_test_score_percent](images/avg_test_score_percent_plot.png)
- 🔼 *Histogram of average test score percent*
- `avg_test_score_percent`
---

## D. Find patterns & correlations
### Preview (Screenshot)
![Correlation Summary](images/corr.png)
- 🔼 *Correlation summary in table format*
- `corr`

![Heatmap](images/heatmap.png)
- 🔼 *Correlation Heatmap of School Factors*
- `heatmap`
---