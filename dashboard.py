pipenv install
pipenv shell
pip install seaborn
pip install matplotlib
pip install streamlit
pip install pandas

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('all_data.csv')

sns.set(style="whitegrid")

# Total bike rentals by weather situation
def total_bike_rentals_by_weather():
    plt.figure(figsize=(10, 6))
    sns.barplot(x='weathersit', y='cnt', data=data, estimator=sum, errorbar=None)
    st.title('Total Bike Rentals by Weather Situation')
    st.write('Weather Situation')
    st.write('Memperlihatkan total penyewaan sepeda berdasarkan situasi cuaca') 
    st.pyplot()

# Working day (0 = No, 1 = Yes)
def total_bike_rentals_by_working_day():
    plt.figure(figsize=(10, 6))
    sns.barplot(x='workingday', y='cnt', data=data, estimator=sum, errorbar=None)
    st.title('Total Bike Rentals by Working Day')
    st.write('Working Day (0 = No, 1 = Yes)')
    st.write('Memperlihatkan total penyewaan sepeda berdasarkan hari kerja')
    st.pyplot()

#  hourly bike rentals
def hourly_bike_rentals():
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='hr', y='cnt', data=data, estimator=sum, errorbar=None)
    st.title('Hourly Bike Rentals')
    st.write('Hour of the Day')
    st.write('Memperlihatkan total penyewaan sepeda berdasarkan jam')
    st.pyplot()

#  weather pattern clustering
def weather_pattern_clustering():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='temp', y='hum', hue='cluster_label', data=data, palette='viridis')
    st.title('Weather Pattern Clustering')
    st.write('Temperature')
    st.write('Humidity')
    st.pyplot()

if __name__ == "__main__":
    total_bike_rentals_by_weather()
    total_bike_rentals_by_working_day()
    hourly_bike_rentals()
    weather_pattern_clustering()
