# Task 1 — Data Immersion & Wrangling
**Internship:** ApexPlanet Software Pvt. Ltd.  
**Domain:** Data Analytics  
**Intern:** Gungun Khatri  

---

## Objective
To acquire, clean, and prepare the Titanic dataset for analysis by handling missing values, removing irrelevant columns, and engineering new features.

---

## Dataset
- **Source:** Kaggle Titanic Dataset
- **Original Shape:** 418 rows × 12 columns
- **Final Shape:** 418 rows × 15 columns

---

## Files in this Repository
| File | Description |
|------|-------------|
| `titanic.csv` | Raw original dataset |
| `cleaning_script.py` | Python script for cleaning & transformation |
| `cleaned_titanic.csv` | Final analysis-ready dataset |
| `data_dictionary.md` | Column descriptions and data quality summary |

---

## What Was Done
1. Loaded and profiled raw data
2. Identified missing values in Age, Fare, Cabin
3. Filled Age and Fare with median values
4. Dropped Cabin column (78% missing)
5. Engineered 4 new columns — AgeGroup, FamilySize, IsAlone, FareCategory
6. Encoded Sex and Embarked to numeric
7. Detected 55 fare outliers using IQR method

---

## Tools Used
- Python, Pandas, NumPy
- VS Code