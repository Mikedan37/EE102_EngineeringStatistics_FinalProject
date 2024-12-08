
import pandas as pd

# Load the dataset
file_path = '/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Gross Domestic Product/Clean Data/Cleaned_GrossDomesticProduct_data.csv'
data = pd.read_csv(file_path)

# Extract the numerical column
column = data['GDP']

# Calculate statistics
mean = column.mean()
median = column.median()
mode = column.mode().iloc[0] if not column.mode().empty else None
minimum = column.min()
maximum = column.max()
variance = column.var()
std_dev = column.std()

# Prepare the statistics report
stats_report = f"""
Statistics Report for Global Competitiveness Index:
----------------------------------------------------
Mean: {mean}
Median: {median}
Mode: {mode}
Minimum: {minimum}
Maximum: {maximum}
Variance: {variance}
Standard Deviation: {std_dev}
"""

# Write the report to a text file
output_file = 'GrossDomesticProduct_Analyzed.txt'
with open(output_file, 'w') as file:
    file.write(stats_report)

print(f"Statistics report saved to {output_file}")
