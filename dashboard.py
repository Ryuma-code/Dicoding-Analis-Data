import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('all_data.csv')

sns.set(style="whitegrid")

# Year selection
year = st.selectbox('Select Year', options=[2011, 2012], format_func=lambda x: f"{x}")

# Filter data based on selected year
data['yr'] = data['yr'].replace({0: 2011, 1: 2012})
filtered_data = data[data['yr'] == year]

# Total bike rentals by weather situation
def total_bike_rentals_by_weather():
    plt.figure(figsize=(10, 6))
    
    # Mapping for weather situation labels
    weather_labels = {1: 'Cerah', 2: 'Berkabut', 3: 'Salju Ringan', 4: 'Hujan Lebat'}
    filtered_data['weathersit_label'] = filtered_data['weathersit'].map(weather_labels)
    
    sns.barplot(x='weathersit_label', y='cnt', data=filtered_data, estimator=sum, errorbar=None)
    st.title('Total Bike Rentals by Weather Situation')
    st.write('Weather Situation')
    st.write('Memperlihatkan total penyewaan sepeda berdasarkan situasi cuaca') 
    st.pyplot()

# Working day (0 = No, 1 = Yes)
def total_bike_rentals_by_working_day():
    plt.figure(figsize=(10, 6))
    
    # Mapping for working day labels
    working_day_labels = {0: 'Holiday', 1: 'Workingday'}
    filtered_data['workingday_label'] = filtered_data['workingday'].map(working_day_labels)
    
    sns.barplot(x='workingday_label', y='cnt', data=filtered_data, estimator=sum, errorbar=None)
    st.title('Total Bike Rentals by Working Day')
    st.write('Working Day (0 = No, 1 = Yes)')
    st.write('Memperlihatkan total penyewaan sepeda berdasarkan hari kerja')
    st.pyplot()

# Hourly bike rentals
def hourly_bike_rentals():
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='hr', y='cnt', data=filtered_data, estimator=sum, errorbar=None)
    st.title('Hourly Bike Rentals')
    st.write('Hour of the Day')
    st.write('Memperlihatkan total penyewaan sepeda berdasarkan jam')
    st.pyplot()

# Weather pattern visualization
def weather_pattern_visualization():
    st.title('Weather Pattern Visualization')
    st.write('Memperlihatkan pola cuaca')
    temp_bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
    hum_bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
    wind_bins = [0, 0.2, 0.4, 0.6, 0.8, 1]

    temp_labels = ["Very Cold", "Cold", "Mild", "Warm", "Hot"]
    hum_labels = ["Very Dry", "Dry", "Moderate", "Humid", "Very Humid"]
    wind_labels = ["Calm", "Light Breeze", "Moderate Wind", "Strong Wind", "Gale"]

    filtered_data['temp_cat'] = pd.cut(filtered_data['temp'], bins=temp_bins, labels=temp_labels, include_lowest=True)
    filtered_data['hum_cat'] = pd.cut(filtered_data['hum'], bins=hum_bins, labels=hum_labels, include_lowest=True)
    filtered_data['wind_cat'] = pd.cut(filtered_data['windspeed'], bins=wind_bins, labels=wind_labels, include_lowest=True)

    filtered_data['weather_pattern'] = filtered_data['temp_cat'].astype(str) + '/' + filtered_data['hum_cat'].astype(str) + '/' + filtered_data['wind_cat'].astype(str)

    plt.figure(figsize=(12, 8))
    sns.scatterplot(x='temp', y='hum', hue='weather_pattern', data=filtered_data, palette='tab20', s=100, style='weather_pattern')

    plt.title('Weather Pattern Clustering with Manual Grouping', fontsize=18)
    plt.xlabel('Normalized Temperature', fontsize=14)
    plt.ylabel('Normalized Humidity', fontsize=14)
    plt.legend(title='Weather Patterns', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    st.pyplot()

if __name__ == "__main__":
    total_bike_rentals_by_weather()
    total_bike_rentals_by_working_day()
    hourly_bike_rentals()
    weather_pattern_visualization()
