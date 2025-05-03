# Netflix 1990s Movies – Exploratory Data Analysis

## Project Overview
This repository contains an end-to-end exploratory data analysis (EDA) of Netflix movies, with a focus on titles released during the 1990s. As a Data Scientist, the goal of this project is to uncover viewing trends, analyze duration patterns, and identify popular genres and international content during this iconic decade in cinema.

## Contents
```
Netflix-EDA/ 
├── data/ 
│      └── netflix_data.csv 
├── notebooks/ 
│         └── notebook_Investigating netflix movies.ipynb
│
├── requirements.txt 
│ 
└── README.txt
```
## Data Description
- **netflix_data.csv**  
  Contains metadata for Netflix titles, including:  
  - `show_id`         — Unique identifier for each title  
  - `type`            — Movie or TV Show  
  - `title`           — Name of the content  
  - `director`        — Director's name  
  - `cast`            — Main cast members  
  - `country`         — Country of origin  
  - `date_added`      — Date it was added to Netflix  
  - `release_year`    — Year the title was originally released  
  - `duration`        — Length of the movie in minutes  
  - `description`     — Short summary of the content  
  - `genre`           — Genre category (Drama, Comedy, etc.)

## Setup & Installation

1. **Install dependencies**

```bash
pip install -r requirements.txt
2. How to Run
 Launch Jupyter Notebook

 jupyter notebook
3. Open notebooks/notebook_Investigating netflix movies.ipynb

4. Execute all cells to reproduce the cleaning, analysis, and visualization steps.
Analysis Highlights
Data Cleaning & Validation
Removed entries not classified as "Movie"

Filtered titles released during the 1990s

Handled missing values in director, country, and duration

Exploratory Visualizations
Distribution of movie durations in the 1990s

Frequency of genres among 1990s movies

Top directors and contributing countries

Yearly trends of releases during the decade

Key Findings
Most movies from the 1990s ranged between 80 and 100 minutes in duration

"Drama" and "Action" were the most dominant genres

The United States contributed the largest volume of 1990s titles

Certain directors consistently appeared with multiple titles in this dataset

Reproducibility & Extensibility
All data processing and visualization code is contained in the notebook.
To extend this project to other decades or include TV shows, simply adjust the filters in the notebook and rerun the analysis.

Dependencies
Python 3.8+

pandas

numpy

matplotlib

seaborn

jupyter

(See requirements.txt for exact versions.)

**License**
This project was extracted from Data Camp scientist's course.

**Contact**
For questions or collaboration inquiries, please contact:
Eliecer Castro

– Data Scientist

– elicasagui@gmail.com

– GitHub: https://github.com/elicasagui/Data-Analysis-.git
