import pandas as pd
import plotly.express as px

from src.load_data import load_csv
from src.clean_data import clean_column_names, parse_dates

def get_data():
    df = load_csv()
    df = clean_column_names(df)
    df = parse_dates(df, ['date_added'])
    movies = df[
        (df.type == 'Movie') &
        (df.release_year.between(1990, 1999))
    ]
    return movies

def most_frequent_duration(movies):
    return int(movies.duration.mode()[0])

def short_action_count(movies):
    action = movies[movies.genre.str.contains('Action', na=False)]
    return int((action.duration < 90).sum())

def fig_duration_hist(movies):
    return px.histogram(
        movies, x='duration', nbins=20,
        title='Duration Distribution (1990s Movies)',
        labels={'duration':'Minutes'},
        template='plotly_dark'
    )

def fig_release_timeseries(movies):
    ts = movies.groupby(pd.Grouper(key='date_added', freq='M')).size().reset_index(name='count')
    return px.line(
        ts, x='date_added', y='count',
        title='Monthly Releases Added to Netflix',
        labels={'date_added':'Date Added','count':'# Titles'},
        template='plotly_dark'
    )

def fig_count_by_year(movies):
    yearly = movies.release_year.value_counts().sort_index().reset_index()
    yearly.columns = ['year','count']
    return px.bar(
        yearly, x='year', y='count',
        title='Movies per Year (1990–1999)',
        labels={'year':'Release Year','count':'Count'},
        template='plotly_dark'
    )

def fig_avg_duration_by_genre(movies):
    exploded = (movies
                .dropna(subset=['genre'])
                .assign(genre=movies.genre.str.split(','))
                .explode('genre'))
    exploded['genre'] = exploded.genre.str.strip()
    avg = exploded.groupby('genre')['duration'].mean().nlargest(10).reset_index()
    return px.bar(
        avg, x='genre', y='duration',
        title='Top 10 Genres by Average Duration',
        labels={'genre':'Genre','duration':'Avg Duration (min)'},
        template='plotly_dark'
    )

def fig_top_directors(movies, top_n=10):
    dirs = (movies.director.dropna()
            .str.split(',')
            .explode()
            .str.strip()
            .value_counts()
            .nlargest(top_n)
            .reset_index())
    dirs.columns = ['director','count']
    return px.bar(
        dirs, x='director', y='count',
        title=f'Top {top_n} Directors by Number of Titles',
        labels={'director':'Director','count':'# Titles'},
        template='plotly_dark'
    )

def fig_short_action_bar(count):
    return px.bar(
        x=['Short Action Movies (<90 min)'], y=[count],
        title='Count of Short Action Movies in the 1990s',
        labels={'x':'Category','y':'Count'},
        template='plotly_dark'
    )

