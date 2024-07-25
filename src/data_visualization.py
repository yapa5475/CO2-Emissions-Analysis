import os
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def load_preprocessed_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    processed_data_path = os.path.join(current_dir, '../data/processed/processed_co2_emissions.csv')
    df = pd.read_csv(processed_data_path)
    return df

def plot_co2_emissions(df, country):
    # Filter data by country
    country_data = df[df['Country Name'] == country]

    # Validate year and CO2 Emissions columns
    # wrong
    if 'Year' in country_data.columns and 'CO2 Emissions' in country_data.columns:
        # Plot CO2 emissions over time
        plt.figure(figsize=(10, 6))
        plt.plot(country_data['Year'], country_data['CO2 Emissions'], marker='o', linestyle='-', color='b')

        # Add titles and labels
        plt.title(f'CO2 Emissions Over Time for {country}')
        plt.xlabel('Year')
        plt.ylabel('CO2 Emissions (kt)')
        plt.grid(True)

        # Show plot
        plt.show()

    else:
        print("There is missing data in the data frame")

def main():
    df = load_preprocessed_data()
    plot_co2_emissions(df, 'United States')

main