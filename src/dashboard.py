import streamlit as st
from src.visualize import (
    get_data,
    most_frequent_duration,
    short_action_count,
    fig_duration_hist,
    fig_release_timeseries,
    fig_genre_bar,
    fig_country_choropleth,
)

st.set_page_config(page_title="Netflix 90s EDA", layout="wide")

movies = get_data()
duration_value = most_frequent_duration(movies)
short_count    = short_action_count(movies)
    
# ——— HEADER METRICS ———
st.title("🎬 Netflix Data Analysis (1990s)")
col1, col2 = st.columns(2)
col1.metric("Most Frequent Duration", f"{duration_value} min")
col2.metric("Short Action Movies", f"{short_count}")

# ——— ROW 1: HISTOGRAM AND TIMESERIES ———
r1c1, r1c2 = st.columns([1,1])
with r1c1:
    st.plotly_chart(fig_duration_hist(movies), use_container_width=True)
with r1c2:
    st.plotly_chart(fig_release_timeseries(movies), use_container_width=True)

# ——— ROW 2: GENRE BAR & COUNTRY MAP ———
r2c1, r2c2 = st.columns([1,1])
with r2c1:
    st.plotly_chart(fig_genre_bar(movies), use_container_width=True)
with r2c2:
    st.plotly_chart(fig_country_choropleth(movies), use_container_width=True)
