
import pandas as pd

# Load the CSV file
file_path = '/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Human Capital Index/Raw Data/HumanCapital_data.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Filter data for the year 2016
filtered_data = data[(data['Year'] == 2016)][['Entity', 'GDP per capita, PPP (constant 2017 international $)']]

# Remove rows where the country name is empty or GDP is 0 or NaN
filtered_data = filtered_data[
    (filtered_data['Entity'].notna()) &
    (filtered_data['Entity'] != '') &
    (filtered_data['GDP per capita, PPP (constant 2017 international $)'] > 0)
]

# Remove duplicate countries if any
filtered_data = filtered_data.drop_duplicates(subset=['Entity'])

# Rename columns to match the desired format
formatted_data = filtered_data.rename(columns={
    'Entity': 'Country',
    'GDP per capita, PPP (constant 2017 international $)': 'GDP'
})

# Save the cleaned and formatted data to a new CSV file
output_path = '/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Human Capital Index/Clean Data/Cleaned_HumanCapital_data.csv'  # Replace with your desired output path
formatted_data.to_csv(output_path, index=False)

print(f"Formatted data has been saved to {output_path}")
