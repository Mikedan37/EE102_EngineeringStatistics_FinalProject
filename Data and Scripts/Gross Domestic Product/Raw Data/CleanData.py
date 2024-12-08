import pandas as pd

# Define the file paths
input_file = r"/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Gross Domestic Product/Raw Data/GrossDomesticProduct_data.csv"  # Update with the actual file name
output_file = r"/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Gross Domestic Product/Clean Data/Cleaned_GrossDomesticProduct_data.csv"

data = pd.read_csv(input_file, skiprows=4)

# Ensure required columns exist
if 'Country Name' not in data.columns or '2016' not in data.columns:
    raise ValueError("Input CSV does not contain the required columns: 'Country Name' and '2016'")

# Select relevant columns and rename them
cleaned_data = data[['Country Name', '2016']].rename(columns={'Country Name': 'Country', '2016': 'GDP'})

# Drop rows with missing GDP values
cleaned_data = cleaned_data.dropna(subset=['GDP'])

# Save the cleaned data to a new CSV file
cleaned_data.to_csv(output_file, index=False)

print(f"Cleaned data saved to {output_file}")
