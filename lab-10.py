import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("my_data.csv", index_col=False)
df = df.drop('Unnamed: 0', axis=1)

# Create a Streamlit app
st.title('YouTube Channel Analysis')

# Add a sidebar for customization
st.sidebar.header('Customization Options')

# Widget to select multiple channel names for comparison
selected_channels = st.sidebar.multiselect('Select Channel Names', df['channel_name'].unique(), default=df['channel_name'].unique()[0])

selected_column = st.sidebar.selectbox('Select Data Column', df['view_count'])

# Filter data based on selected channel names
filtered_data = df[df['channel_name'].isin(selected_channels)]

# Create the histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=filtered_data, x=selected_column, hue='channel_name', multiple="stack", discrete=True, palette='tab10')

# Customize the plot
plt.xlabel(selected_column.capitalize())
plt.ylabel('Count')
plt.title(f'Distribution of {selected_column.capitalize()} Among Selected Channels')

# Show the legend
plt.legend(title='Channel Name', bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the plot in the Streamlit app
st.pyplot(plt)

