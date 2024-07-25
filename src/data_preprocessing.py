import pandas as pd
import os

def load_data(filepath):
    return pd.read_csv(filepath)

def main():
    print('Executing data pre processing... ')

    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir.replace('/src', '/data/raw/API_EN.ATM.CO2E.KT_DS2_en_csv_v2_1338275.csv'))
    processed_data_path = os.path.join(current_dir.replace('/src', '/data/processed/processed_co2_emissions.csv'))

    try:
        df = pd.read_csv(data_path, delimiter=',',skiprows=4,header=0)
    except pd.errors.ParserError as e:
        print(f"Failed to read the CSV file: {e}")
        return

    df = preprocess_data(df)
    save_data(df, processed_data_path)
    print(f"Data saved to {processed_data_path}")


def preprocess_data(df):
    df.fillna(0, inplace=True)
    return df

def save_data(df, filepath):
    df.to_csv(filepath, index=False)

main()