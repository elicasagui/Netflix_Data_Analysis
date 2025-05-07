# Netflix 1990s Movies – Exploratory Data Analysis

## Project Overview
This repository contains an end-to-end exploratory data analysis (EDA) of Netflix movies, with a focus on titles released during the 1990s. As a Data Scientist, the goal of this project is to uncover viewing trends, analyze duration patterns, and identify popular genres and international content during this iconic decade in cinema.

## Contents
```
Netflix_Data_Analysis/
├── data/ # CSV files go here
│ └── netflix_titles.csv
│
├── notebooks/ # Jupyter notebooks for EDA and testing
│ └── images/
│ └── exploratory_analysis.ipynb
│ └── test/
├── src/ # Source code for analysis
│ ├── init.py # Makes src a Python package
│ ├── load_data.py # Functions to load datasets
│ ├── clean_data.py # Cleaning and preprocessing functions
│ ├── analyze.py # EDA and summary statistics
│ ├── visualize.py # Plotting functions (e.g., seaborn/matplotlib)
│ └── utils.py # Helper functions
├── main.py # Main execution script
├── requirements.txt # Python dependencies
└── README.md # This file

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

## Data Instructions

**1. Download dataset from Kaggle**

https://www.kaggle.com/datasets/shivamb/netflix-shows

**2. Move the downloaded CSV file into the `data/` directory**

```
mkdir -p data/
mv ~/Downloads/netflix_titles.csv data/
```
## Setup & Installation

**1. Clone the repository:**
   ```
   git clone https://github.com/elicasagui/Netflix_Data_Analysis.git
   cd Netflix_Data_Analysis
```
**2. (Optional) Create and activate a virtual environment**
```
python -m venv venv
```
On Windows
```
.\venv\Scripts\Activate
```
On macOS/Linux
```
source venv/bin/activate
```
**If PowerShell blocks script activation, run this command in PowerShell (as Administrator):**
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
Then activate the environment again:
```
.\venv\Scripts\Activate
```
**3. Install dependencies**
```
pip install -r requirements.txt
```
**4. Run the main script**
```
python main.py
```
**5. Launch Jupyter Notebook**
```
 jupyter notebook
 ```
**6. Open and run the notebook**
```
notebooks/exploratory_analysis.ipynb
```
## Running tests
**1. Install pytest:**
```
pip install pytest
```
**2. Run tests:**
```
pytest tests/
```

## Project Questions
1. What is the most common type of content on Netflix?
2. Which countries produce the most Netflix content?
3. What genres are most frequently listed?
4. What are the trends in releases over time?

## Key Insights
Insight ID	Description	Visualization
1	Distribution of content types (Movies vs. TV Shows)	
2	Top countries by content volume	
3	Most popular genres on the platform	

Full analysis available in exploratory_analysis.ipynb.

## Dependencies
Python 3.8+

pandas

numpy

matplotlib

seaborn

jupyter

(See requirements.txt for exact versions.)

## License
This project was extracted from Data Camp scientist's course.

## Contact
For questions or collaboration inquiries, please contact:
Eliecer Castro

– Data Scientist

– elicasagui@gmail.com

– GitHub: https://github.com/elicasagui/Data-Analysis-.git
