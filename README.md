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
├── data/                             # (empty or contains raw files)
├── notebooks/
│   ├── exploratory_analysis.ipynb
│   └── images/
│       └── netflix_movies_duration.png
├── src/
│   ├── data/
│   │   ├── load_data.py
│   │   └── clean_data.py
│   └── visualization/
│       └── plot.py
├── .gitignore
├── README.md
└── requirements.txt
</code></pre>

  <h2>📊 Data Description</h2>
  <p>The <code>netflix_data.csv</code> file includes movie and show metadata such as:</p>
  <ul>
    <li><strong>show_id</strong> – Unique identifier of the show</li>
    <li><strong>type</strong> – “Movie” or “TV Show”</li>
    <li><strong>title</strong> – Title of the show</li>
    <li><strong>director</strong> – Director(s) of the show</li>
    <li><strong>cast</strong> – Main cast members</li>
    <li><strong>country</strong> – Country of origin</li>
    <li><strong>date_added</strong> – Date the show was added to Netflix</li>
    <li><strong>release_year</strong> – Year the show was released</li>
    <li><strong>duration</strong> – Duration in minutes (for movies) or number of seasons</li>
    <li><strong>description</strong> – Brief synopsis of the show</li>
    <li><strong>genre</strong> – Genre(s) of the show</li>
  </ul>

  <h2>🔧 Setup &amp; Installation</h2>
  <ol>
    <li>
      <strong>Clone the repository</strong><br>
      <pre><code>git clone https://github.com/elicasagui/Netflix_Data_Analysis.git
cd Netflix_Data_Analysis</code></pre>
    </li>
    <li>
      <strong>Create a virtual environment</strong><br>
      <pre><code>python -m venv venv</code></pre>
    </li>
    <li>
      <strong>Activate the virtual environment (PowerShell)</strong><br>
      <pre><code>Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate</code></pre>
      <em>— this temporarily allows script execution and then activates the venv</em>
    </li>
    <li>
      <strong>Install dependencies</strong><br>
      <pre><code>python -m pip install --upgrade pip
python -m pip install -r requirements.txt</code></pre>
    </li>
 
  <h2>Usage</h2>
  <p>Launch JupyterLab:</p>
  <pre><code>jupyter lab</code></pre>
  <p>Or, if not recognized:</p>
  <pre><code>python -m jupyterlab</code></pre>
  <p>Run tests:</p>
  <pre><code>python -m pytest</code></pre>
  <p>Ensure all tests in the <code>tests/</code> directory pass.</p>
</body>
</html>
  </ol>

  <h2>📈 Key Insights</h2>
  <ul>   
  <li>
    <strong>Most Frequent Movie Duration in the 1990s:</strong>  
    Approximately <code>94</code> minutes.<br>
    <pre><code># duration = 94</code></pre>
  </li>
  <li>
    <strong>Number of Short Action Movies (&lt; 90 min) in the 1990s:</strong>  
    <code>7</code>.<br>
    <pre><code># short_movie_count = 7</code></pre>
    <img 
      src="notebooks/images/netflix _movies_duration.png" 
      alt="Distribution of Movie Durations" 
      style="max-width:40%; height:auto; border:1px solid #ccc; margin-top:0.5em;"
    />
  </li>
</ul>

  <h2>📄 License</h2>
  <p>This project was developed during a DataCamp data science course..</p>
  
<h2>📄 Created by </h2>
<p>Eliecer Castro</p>
<p>Data Scientist<p>

</body>
</html>



