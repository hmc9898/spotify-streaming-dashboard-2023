import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from matplotlib import pyplot as plt
#import need libraries
df=pd.read_csv(r'C:\Users\hcull\datasets\spotify_2023.csv')
#read file
st.title("Spotify Most Streamed Songs in 2023")
st.header("Interactive Scatter Plot of Spotify Charts Based on BPM")
fig1= px.scatter(
    df,
    x='bpm',
    y='in_spotify_charts',
    title="Number on Spotify Charts Based on BPM",
    labels={"bpm": "BPM", "in_spotify_charts": "Number on Spotify Charts"},
    opacity=0.5
)
st.plotly_chart(fig1)
#scatterplot labeled as fig1
st.header("Interactive Histogram: Number if Songs Released by Year")
fig2= px.histogram(
    df,
    x='released_year',
    nbins=30,
    title="Number of Songs Released by Year on Spotify's Most Streamed",
    labels={"released_year": "Released Year", "count": "Count"},
    opacity=0.5
)
fig2.update_xaxes(
    tickmode="array",
    tickvals=np.arange(int(df['released_year'].min()), int(df['released_year'].max()) + 1,10),
    tickangle=45
)
st.plotly_chart(fig2)
#hisogram titled fig2
st.header("Spotify Song Releases by Month")
month_counts = df['released_month'].value_counts().sort_index()
highest_month = month_counts.idxmax()
fig3, ax = plt.subplots()
bars = ax.bar(month_counts.index, month_counts, edgecolor='black', alpha=0.7)
if st.checkbox("Highest Month in Red"):
    for bar, month in zip(bars, month_counts.index):
        if month == highest_month:
            bar.set_color('red')  # Highlight the highest month in red
        else:
            bar.set_color('gray')  # Other bars remain gray
else:
    for bar in bars:
        bar.set_color('blue')
ax.set_xlabel('Release Month')
ax.set_ylabel('Song Count')
ax.set_title("Song Releases by Month on Spotify's Most Streamed")
ax.set_xticks(range(1, 13))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
st.pyplot(fig3)
#Checkbox labeled fig3