import pandas as pd
import plotly.express as px

from src.load_data import load_csv
from src.clean_data import clean_column_names, parse_dates

def get_data():
    df = load_csv()
    df = clean_column_names(df)
    # convert date_added to datetime
    df = parse_dates(df, ['date_added'])
    # filter 1990s movies
    movies = df[
        (df.type == 'Movie') &
        (df.release_year.between(1990, 1999))
    ]
    return movies

def most_frequent_duration(movies: pd.DataFrame) -> int:
    return int(movies.duration.mode()[0])

def short_action_count(movies: pd.DataFrame) -> int:
    action = movies[movies.genre.str.contains('Action', na=False)]
    return int((action.duration < 90).sum())

def fig_duration_hist(movies: pd.DataFrame):
    return px.histogram(
        movies, x='duration', nbins=20,
        title='Duration Distribution (1990s Movies)',
        labels={'duration':'Minutes'},
        template='plotly_dark'
    )

def fig_release_timeseries(movies: pd.DataFrame):
    # group by when added
    ts = movies.groupby(pd.Grouper(key='date_added', freq='M')).size().reset_index(name='count')
    return px.line(
        ts, x='date_added', y='count',
        title='Monthly Releases Added to Netflix',
        labels={'date_added':'Date Added','count':'# of Titles'},
        template='plotly_dark'
    )

def fig_genre_bar(movies: pd.DataFrame):
    # explode genres
    genres = movies.genre.dropna().str.split(',').explode().str.strip()
    top = genres.value_counts().nlargest(10).reset_index()
    top.columns = ['genre','count']
    return px.bar(
        top, x='genre', y='count',
        title='Top 10 Genres (1990s Movies)',
        labels={'genre':'Genre','count':'Count'},
        template='plotly_dark'
    )

def fig_country_choropleth(movies: pd.DataFrame):
    cnt = movies.country.str.split(',').explode().str.strip().value_counts().reset_index()
    cnt.columns = ['country','count']
    return px.choropleth(
        cnt, locations='country', locationmode='country names',
        color='count', hover_name='country',
        title='Titles by Country of Origin',
        template='plotly_dark'
    )
