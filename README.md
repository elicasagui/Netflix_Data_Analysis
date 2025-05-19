<!DOCTYPE html>
<html lang="en">

<body>

  <h1>Netflix Data Analysis – Exploratory Data Analysis with Python</h1>

  <h2>Project Overview</h2>
  <p>
    This project performs an exploratory data analysis (EDA) on Netflix titles to discover trends and patterns in the available content. It uses Python libraries such as pandas, matplotlib, and seaborn. The goal is to analyze movie metadata from the 1990s.
  </p>

  <h2>📁 Repository Structure</h2>
  <pre><code>Netflix_Data_Analysis/
├── data/
│   ├── raw/                 # Original dataset (e.g., netflix_titles.csv)
│   └── processed/           # Cleaned data
├── notebooks/
│   └── exploratory_analysis.ipynb
│   └── images/              # Graphs for analysis
├── src/
│   ├── data/                # Data loading and cleaning scripts
│   └── visualization/       # Plotting functions
├── requirements.txt
├── README.md
└── LICENSE
</code></pre>

  <h2>📊 Dataset</h2>
  <ul>
    <li><strong>Source:</strong> <a href="https://www.kaggle.com/datasets/shivamb/netflix-shows" target="_blank">Netflix Titles Dataset on Kaggle</a></li>
    <li><strong>Key columns:</strong> <code>title</code>, <code>type</code>, <code>release_year</code>, <code>duration</code>, <code>genre</code>, etc.</li>
  </ul>

  <h2>🔧 Setup &amp; Installation</h2>
  <ol>
    <li>
      <strong>Clone the repository</strong><br>
      <pre><code>git clone https://github.com/elicasagui/Netflix_Data_Analysis.git
cd Netflix_Data_Analysis
</code></pre>
    </li>
    <li>
      <strong>Install dependencies</strong><br>
      <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>
      <strong>Launch Jupyter Notebook</strong><br>
      <pre><code>jupyter notebook</code></pre>
    </li>
  </ol>

  <h2>📈 Key Insights</h2>
  <ul>
    <li>
      <strong>Most Frequent Movie Duration in the 1990s:</strong>  
      Approximately <code>100</code> minutes.<br>
      <pre><code># duration = 100</code></pre>
    </li>
    <li>
      <strong>Number of Short Action Movies (&lt; 90 min) in the 1990s:</strong>  
      <code>7</code>.<br>
      <pre><code># short_movie_count = 7</code></pre>
      <img src="notebooks/images/netflix_movies_duration.png" alt="Distribution of Movie Durations" />
    </li>
  </ul>

  <h2>📄 License</h2>
  <p>Distributed under the MIT License.</p>

</body>
</html>


