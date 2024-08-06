import os
import pandas as pd
import argparse
# don't push this, make it so that you can debug via a terminal command.
# maybe make something like this work:
# python data_analysis.py ../data/processed/processed_co2_emissions.csv --debug


def load_preprocessed_data(filepath, debug=False):
    """
    Load preprocessed data from a specified file path.

    Parameters:
    filepath (str): Path to the CSV file containing the preprocessed data.

    Returns:
    pd.DataFrame: Loaded data as a pandas DataFrame.
    """
    print(filepath)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    processed_data_path = os.path.join(current_dir, filepath)
    df = pd.read_csv(processed_data_path)
    return df

def summarize_stats(df, debug=False):
    """
    Print summary statistics of the DataFrame.

    Parameters:
    df (pd.DataFrame): DataFrame containing the data.
    """
    summary_stats = df.describe()
    print("Summary statistics: ")
    print(summary_stats)

def main(filepath, debug=False):
    """
    Main function to load data and print summary statistics.

    Parameters:
    filepath (str): Path to the CSV file to be processed.
    """
    # processed_co2_emissions_file = '../data/processed/processed_co2_emissions.csv'
    df = load_preprocessed_data(filepath)
    summarize_stats(df)

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Process and summarize CO2 emissions data.')
    parser.add_argument('filepath', type=str, help='Path to the CSV file containing the data.')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode.')


    # Parse arguments
    args = parser.parse_args()

    # Run main function with the provided file path
    main(args.filepath)