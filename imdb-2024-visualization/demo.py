import streamlit as st
import pandas as pd
import numpy as np

st.title("project I")
st.header("IMDB 2024 Data Scraping and Visualizations")
df = pd.read_csv("C:/Users/kanis/Downloads/IMDb_2024_Top10_With_Genres.csv")
st.write(df)
st.line_chart(df,y=['Rating'])
st.line_chart(df,y=['Votes'])
st.bar_chart(df,y=['Year'])
st.bar_chart(df,y=['Duration (min)'])
st.area_chart(df,y=['Votes'])
st.bar_chart(df,y=['Metascore'])

