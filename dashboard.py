import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
file_path = 'cleaned_dataset.csv'  # Replace with the file path if necessary
data = pd.read_csv(file_path)

# Set Streamlit page configuration
st.set_page_config(page_title="Air Quality and Weather Analysis Dashboard", layout="wide")

# Title and Description
st.title("Air Quality and Weather Analysis Dashboard")
st.write("""
This dashboard helps analyze how weather conditions affect air pollution levels, 
especially PM2.5 and PM10, and identifies seasonal and daily patterns in pollution levels.
""")

# Sidebar filters
st.sidebar.header("Filters")
selected_year = st.sidebar.selectbox("Select Year", sorted(data['year'].unique()))
data = data[data['year'] == selected_year]

# Filtered Data for Selected Year
st.write(f"### Air Quality Data for Year: {selected_year}")
st.dataframe(data.head())

# Part 1: Correlation Analysis between Weather and Pollution
st.header("Weather Conditions vs Air Pollution Levels")
weather_cols = ['TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']
pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']

# Correlation Heatmap
st.subheader("Correlation Heatmap")
corr = data[weather_cols + pollutants].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
st.pyplot(plt)

# Scatter plots for selected weather variables and PM2.5, PM10
st.subheader("Scatter Plots: Weather vs. PM2.5 and PM10")
weather_feature = st.selectbox("Select Weather Feature", weather_cols)
plt.figure(figsize=(12, 6))
sns.scatterplot(data=data, x=weather_feature, y="PM2.5", label="PM2.5", alpha=0.5)
sns.scatterplot(data=data, x=weather_feature, y="PM10", label="PM10", alpha=0.5)
plt.title(f"{weather_feature} vs PM2.5 and PM10")
plt.xlabel(weather_feature)
plt.ylabel("Pollutant Concentration")
st.pyplot(plt)

# Part 2: Seasonal Patterns in Pollution Levels
st.header("Seasonal and Daily Patterns in Pollution Levels")

# Monthly average pollutant concentrations
st.subheader("Monthly Average Pollutant Levels")
monthly_data = data.groupby('month')[pollutants].mean()
plt.figure(figsize=(12, 6))
monthly_data.plot(marker='o')
plt.title("Monthly Average Pollutant Concentrations")
plt.xlabel("Month")
plt.ylabel("Concentration (µg/m³)")
plt.legend(title="Pollutants")
st.pyplot(plt)

# Hourly average pollutant concentrations
st.subheader("Hourly Average Pollutant Levels")
hourly_data = data.groupby('hour')[pollutants].mean()
plt.figure(figsize=(12, 6))
hourly_data.plot(marker='o')
plt.title("Hourly Average Pollutant Concentrations")
plt.xlabel("Hour of the Day")
plt.ylabel("Concentration (µg/m³)")
plt.legend(title="Pollutants")
st.pyplot(plt)

# Conclusion and Insights
st.header("Conclusions and Insights")
st.write("""
- The **correlation heatmap** allows us to see how weather variables relate to different pollutant levels.
- The **scatter plots** between selected weather features and pollutants (PM2.5, PM10) reveal direct relationships.
- **Monthly and hourly trends** indicate seasonal and daily pollution patterns, helping to identify critical times for pollution control.
""")
