<h1>Netflix Data Analysis – Exploratory Data Analysis with Python</h1>

<h2>Project Overview</h2>
<p>
This project performs an exploratory data analysis (EDA) on Netflix titles to discover trends and patterns in the available content. It uses Python libraries such as pandas, matplotlib, and seaborn. The goal is to analyze movie and TV show metadata to identify popular genres, release trends, duration patterns, and country distributions.
</p>

<h2>📁 Repository Structure</h2>
<pre><code>
Netflix_Data_Analysis/
├── data/
│   ├── raw/                 # Original dataset (e.g., netflix_titles.csv)
│   └── processed/           # Cleaned data
├── notebooks/
│   ├── exploratory_analysis.ipynb
│   └── images/              # Graphs for analysis
├── src/
│   ├── data/                # Data loading and cleaning scripts
│   ├── visualization/       # Plotting functions
├── requirements.txt
├── README.md
└── LICENSE
</code></pre>

<h2>📊 Dataset</h2>
<ul>
  <li><strong>Source:</strong> <a href="https://www.kaggle.com/datasets/shivamb/netflix-shows" target="_blank">Netflix Titles Dataset on Kaggle</a></li>
  <li><strong>Columns include:</strong> title, type, director, cast, country, release_year, rating, duration, genre, etc.</li>
</ul>

<h2>🔧 Setup & Installation</h2>

<h3>1. Clone the repository</h3>
<pre><code>git clone https://github.com/elicasagui/Netflix_Data_Analysis.git
cd Netflix_Data_Analysis
</code></pre>

<h3>2. (Optional) Create a virtual environment</h3>
<pre><code>python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
</code></pre>

<h3>3. Install dependencies</h3>
<pre><code>pip install -r requirements.txt
</code></pre>

<h3>4. Launch Jupyter Notebook</h3>
<pre><code>jupyter notebook
</code></pre>

<h2>📈 Key Insights (Sample Visualizations)</h2>

<h3>Content by Year</h3>
<p><img src="notebooks/images/content_by_year.png" alt="Content by Year" width="600"/></p>

<h3>Top 10 Countries with Most Titles</h3>
<p><img src="notebooks/images/top_countries.png" alt="Top Countries" width="600"/></p>

<h3>Movie Duration Distribution</h3>
<p><img src="notebooks/images/duration_distribution.png" alt="Duration Distribution" width="600"/></p>

<h2>✅ Conclusions</h2>
<ul>
  <li>The number of Netflix releases peaked in recent years, especially 2019–2020.</li>
  <li>The U.S. and India contribute the largest volume of content.</li>
  <li>Most movies are around 90 minutes long, while TV Shows often have 1–2 seasons.</li>
  <li>Popular genres include Drama, Comedy, and Documentary.</li>
</ul>

<h2>📌 Future Work</h2>
<ul>
  <li>Add interactive visualizations using Plotly or Tableau</li>
  <li>Build a content recommendation model</li>
  <li>Analyze sentiment from descriptions or reviews (if available)</li>
</ul>

<h2>📄 License</h2>
<p>Distributed under the MIT License.</p>

<h2>📚 Acknowledgments</h2>
<ul>
  <li><a href="https://www.kaggle.com/datasets/shivamb/netflix-shows" target="_blank">Netflix dataset on Kaggle</a></li>
  <li>Inspired by various EDA projects and dashboards</li>
</ul>

