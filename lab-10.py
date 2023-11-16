import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("my_data.csv", index_col=False)
df = df.drop('Unnamed: 0', axis=1)

# Create a Streamlit app
st.title("YouTube Analytics")

# Sidebar to select channel name, metric, and year
selected_channel = st.sidebar.selectbox("Select Channel Name", df['channel_name'].unique())
selected_metric = st.sidebar.selectbox("Select Metric", ['view_count', 'like_count', 'comment_count'])
selected_year = st.sidebar.slider("Select Year", min_value=df['year'].min(), max_value=df['year'].max())

# Filter the DataFrame based on the selected channel, metric, and year
filtered_df = df[(df['channel_name'] == selected_channel) & (df['year'] == selected_year)]

# Create a line chart of the selected metric over time
fig = px.line(filtered_df, x='published', y=selected_metric, title=f'{selected_metric.capitalize()} Over Time for {selected_channel} in {selected_year}')
fig.update_xaxes(title='Published Date')
fig.update_yaxes(title=selected_metric.capitalize())

# Display the chart
st.plotly_chart(fig)


