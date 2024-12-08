import pandas as pd

# Load the provided CSV file
file_path = '/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Human Capital Index/Clean Data/Cleaned_HumanCapital_data.csv'  # Replace with the actual path to your file
data = pd.read_csv(file_path)

# Apply normalization using the formula: (x - min(x)) / (max(x) - min(x))
normalized_data = data.copy()

# Normalize all numeric columns
numeric_columns = normalized_data.select_dtypes(include='number').columns
for column in numeric_columns:
    min_val = normalized_data[column].min()
    max_val = normalized_data[column].max()
    normalized_data[column] = (normalized_data[column] - min_val) / (max_val - min_val)

# Save the normalized data to a new CSV file
output_path = '/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Human Capital Index/Normalized Data/Normalized_GlobalCompetitiveness_data.csv'  # Replace with the desired output path
normalized_data.to_csv(output_path, index=False)

print(f"Normalized data has been saved to: {output_path}")


