import pandas as pd

# Load the CSV file
file_path = '/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/World Governance/Raw Data/WorldwideGovernance_data.csv'  # Replace with the correct path
data = pd.read_csv(file_path)

# Filter rows where 'Series Code' is 'CC.EST'
filtered_data = data[data['Series Code'] == 'PV.EST']

# Select relevant columns: 'Country Name' and '2016 [YR2016]'
cleaned_data = filtered_data[['Country Name', '2016 [YR2016]']]

# Remove rows with blank, zero, or '..' values in '2016 [YR2016]'
cleaned_data = cleaned_data[cleaned_data['2016 [YR2016]'].notnull()]
cleaned_data = cleaned_data[cleaned_data['2016 [YR2016]'] != 0]
cleaned_data = cleaned_data[cleaned_data['2016 [YR2016]'] != '..']

# Remove duplicates to ensure one row per country
cleaned_data = cleaned_data.drop_duplicates(subset='Country Name')

# Save the cleaned data to a new CSV file
output_path = '/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/World Governance/Clean Data/Cleaned_WorldwideGovernance_data.csv'  # Replace with desired output path
cleaned_data.to_csv(output_path, index=False)

# Print the number of unique countries
print(f"Number of unique countries: {cleaned_data['Country Name'].nunique()}")
