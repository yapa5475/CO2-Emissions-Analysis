# CO2-Emissions-Analysis
A small project for analyzing carbon dioxide emissions

## Initial Setup
- Create a basic repository
- Create directory and basic file structure
- Create a virtual environment
- Strart with data loading and preprocessing

## How to run
1. Create a virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

2. Install required packages
There's already a `requirements.txt` file. To install those requrements, run
```
pip install -r requrements.txt
```

# Running individual files
1. data_analysis.py
- change to the src/ directory
```
python data_analysis.py ../data/processed/processed_co2_emissions.csv
```

Example output
```
../data/processed/processed_co2_emissions.csv
Summary statistics: 
        1960   1961   1962   1963   1964   1965   1966  ...          2018          2019          2020   2021   2022   2023  Unnamed: 68
count  266.0  266.0  266.0  266.0  266.0  266.0  266.0  ...  2.660000e+02  2.660000e+02  2.660000e+02  266.0  266.0  266.0        266.0
mean     0.0    0.0    0.0    0.0    0.0    0.0    0.0  ...  1.211818e+06  1.215004e+06  1.167400e+06    0.0    0.0    0.0          0.0
std      0.0    0.0    0.0    0.0    0.0    0.0    0.0  ...  4.130673e+06  4.155548e+06  4.024503e+06    0.0    0.0    0.0          0.0
min      0.0    0.0    0.0    0.0    0.0    0.0    0.0  ...  0.000000e+00  0.000000e+00  0.000000e+00    0.0    0.0    0.0          0.0
25%      0.0    0.0    0.0    0.0    0.0    0.0    0.0  ...  1.570400e+03  1.639575e+03  1.482600e+03    0.0    0.0    0.0          0.0
50%      0.0    0.0    0.0    0.0    0.0    0.0    0.0  ...  1.866480e+04  1.909435e+04  1.891585e+04    0.0    0.0    0.0          0.0
75%      0.0    0.0    0.0    0.0    0.0    0.0    0.0  ...  2.291706e+05  2.279728e+05  2.149109e+05    0.0    0.0    0.0          0.0
max      0.0    0.0    0.0    0.0    0.0    0.0    0.0  ...  3.556056e+07  3.547725e+07  3.356643e+07    0.0    0.0    0.0          0.0

[8 rows x 65 columns]
```
