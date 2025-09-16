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

![Checking Missing values](images/isnull.png)
- 🔼 *Checks if we have any missing values*
- `df.isnull().sum()`

![Checking duplicate values](images/duplicate.png)
- 🔼 *Checks if we have any duplicates*
- `df.duplicated().sum()`
---

## A. Data Quality Check
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
![Bar graph of schools by type](images/school_by_state.png)
- 🔼 *Bar Graph on schools by type*
- `school_by_type`

![Histogram of funding_per_student_usd](images/school_by_type.png)
- 🔼 *Histogram of funding per student (in usd)*
- `funding_per_student_usd`

![Histogram of avg_test_score_percent](images/school_by_level.png)
- 🔼 *Histogram of average test score percent*
- `avg_test_score_percent`
---