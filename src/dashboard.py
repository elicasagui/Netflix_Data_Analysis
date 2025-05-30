# src/dashboard.py

import os
import sys

# ─── Fix import path so that 'src' is on sys.path ─────────────────────────
# Replace the first element (which Streamlit sets to the script’s folder)
# with your project root (one level up from this file).
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path[0] = project_root
# ─────────────────────────────────────────────────────────────────────────

import streamlit as st
from src.visualize import (
    get_data,
    most_frequent_duration,
    short_action_count,
    fig_duration_hist,
    fig_release_timeseries,
    fig_count_by_year,
    fig_avg_duration_by_genre,
    fig_top_directors,
    fig_short_action_bar
)

# Streamlit page config
st.set_page_config(page_title="Netflix 90s Dashboard", layout="wide")

# Load data
movies = get_data()

# Sidebar filters
st.sidebar.header("Filters")
year_range = st.sidebar.slider("Release Year", 1990, 1999, (1990, 1999))
all_genres = sorted(
    {g.strip() for s in movies.genre.dropna().str.split(',') for g in s}
)
selected_genres = st.sidebar.multiselect("Genres", all_genres, default=all_genres)

# Apply filters
df = movies[movies.release_year.between(*year_range)]
if selected_genres:
    pattern = '|'.join(selected_genres)
    df = df[df.genre.str.contains(pattern, na=False)]

# Key metrics
dur_val   = most_frequent_duration(df)
short_cnt = short_action_count(df)
total_cnt = len(df)
col1, col2, col3 = st.columns(3)
col1.metric("Most Frequent Duration", f"{dur_val} min")
col2.metric("Short Action Movies", f"{short_cnt}")
col3.metric("Total Movies Selected", f"{total_cnt}")

# Title
st.title("🎬 Netflix Data Analysis (1990s)")

# Row 1: Hist & Yearly Count
r1c1, r1c2 = st.columns(2)
with r1c1:
    st.plotly_chart(fig_duration_hist(df), use_container_width=True)
with r1c2:
    st.plotly_chart(fig_count_by_year(df), use_container_width=True)

# Row 2: Avg Duration by Genre & Top Directors
r2c1, r2c2 = st.columns(2)
with r2c1:
    st.plotly_chart(fig_avg_duration_by_genre(df), use_container_width=True)
with r2c2:
    st.plotly_chart(fig_top_directors(df), use_container_width=True)

# Full-width charts: Time Series & Short-Action Bar
st.plotly_chart(fig_release_timeseries(df), use_container_width=True)
st.plotly_chart(fig_short_action_bar(short_cnt), use_container_width=True)
