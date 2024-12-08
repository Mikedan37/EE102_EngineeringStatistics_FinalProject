import pandas as pd

# Load the dataset
file_path = '/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Global Competitiveness Index/Raw Data/GlobalCompetitiveness_data.csv'

# Read the data
data = pd.read_csv(file_path)

# Extract country names and Global Competitiveness Index row
country_names = data.iloc[2, 8:]  # Row 2 for country names
gci_values = data.iloc[3, 8:]    # Row 4 for Global Competitiveness Index values

# Create a cleaned DataFrame
cleaned_data = pd.DataFrame({
    'Country': country_names.values,
    'GlobalCompetitivenessIndex': gci_values.values
})

# Drop rows with missing values
cleaned_data.dropna(inplace=True)

# Save the cleaned data to a CSV file
output_path = '/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Global Competitiveness Index/Clean Data/Cleaned_GlobalCompetitiveness_data.csv'
cleaned_data.to_csv(output_path, index=False)

print(f"Cleaned data saved to {output_path}")
print(f"Number of countries listed: {cleaned_data.shape[0]}")
