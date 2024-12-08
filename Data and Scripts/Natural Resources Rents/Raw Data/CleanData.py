import pandas as pd

# Load the CSV file
file_path = '/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Natural Resources Rents/Raw Data/NaturalResources_data.csv'
data = pd.read_csv(file_path)

# Filter rows where 'Series Code' is 'PV.EST'
filtered_data_pv = data[data['Series Code'] == 'PV.EST']

# Select relevant columns: 'Country Name' and '2016 [YR2016]'
cleaned_data_pv = filtered_data_pv[['Country Name', '2016 [YR2016]']]

# Remove rows with blank, zero, or '..' values in '2016 [YR2016]'
cleaned_data_pv = cleaned_data_pv[cleaned_data_pv['2016 [YR2016]'].notnull()]
cleaned_data_pv = cleaned_data_pv[cleaned_data_pv['2016 [YR2016]'] != 0]
cleaned_data_pv = cleaned_data_pv[cleaned_data_pv['2016 [YR2016]'] != '..']

# Remove duplicates to ensure one row per country
cleaned_data_pv = cleaned_data_pv.drop_duplicates(subset='Country Name')

# Sort by '2016 [YR2016]' in descending order
sorted_data_pv = cleaned_data_pv.sort_values(by='2016 [YR2016]', ascending=False)

# Save the sorted data to a new CSV file
output_path = ''  # Replace with desired output path
sorted_data_pv.to_csv(output_path, index=False)

# Print the top 5 rows for verification
print(sorted_data_pv.head())
