# Data Dictionary — Titanic Dataset
**Source:** Kaggle Titanic Dataset  
**Cleaned by:** Gungun Khatri  
**Date:** June 2026

---

## Original Columns

| Column | Type | Description | Business Relevance |
|--------|------|-------------|-------------------|
| PassengerId | int | Unique ID for each passenger | Identifier only |
| Survived | int | 0 = No, 1 = Yes | Target variable |
| Pclass | int | Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd) | Socioeconomic status indicator |
| Name | object | Full name of passenger | Identity, not used in analysis |
| Sex | int | Gender (0 = male, 1 = female) | Key survival factor |
| Age | float | Age in years (86 nulls filled with median) | Demographic segmentation |
| SibSp | int | No. of siblings/spouses aboard | Family structure |
| Parch | int | No. of parents/children aboard | Family structure |
| Ticket | object | Ticket number | No analytical value |
| Fare | float | Passenger fare in pounds (1 null filled with median) | Proxy for wealth |
| Cabin | object | Cabin number (dropped — 78% missing) | Too incomplete to use |
| Embarked | int | Port of embarkation (0=S, 1=C, 2=Q) | Geographic indicator |

---

## Engineered Columns

| Column | Type | Description | How Created |
|--------|------|-------------|-------------|
| AgeGroup | category | Age bracket | Cut from Age: Child/Teen/Young Adult/Adult/Senior |
| FamilySize | int | Total family members aboard | SibSp + Parch + 1 |
| IsAlone | int | 1 if travelling alone | FamilySize == 1 |
| FareCategory | category | Fare bracket | Cut from Fare: Low/Medium/High/Very High |

---

## Data Quality Summary

| Issue | Column | Action Taken |
|-------|--------|--------------|
| 86 missing values | Age | Filled with median (27.0) |
| 1 missing value | Fare | Filled with median |
| 327 missing values (78%) | Cabin | Column dropped |
| 0 duplicates | — | No action needed |
| 55 outliers detected | Fare | Kept, noted for analysis |