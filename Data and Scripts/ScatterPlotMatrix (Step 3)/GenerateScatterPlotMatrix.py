import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define file paths for each variable's data (replace with actual file paths)
file_paths = {
    "GlobalCompetitivenessIndex": "/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Global Competitiveness Index/Clean Data/Cleaned_GlobalCompetitiveness_data.csv",
    "GlobalInnovationIndex": "/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Global Innovation Index/Clean Data/Cleaned_GlobalInnovation_data.csv",
    "HumanCapitalIndex": "/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Human Capital Index/Clean Data/Cleaned_HumanCapital_data.csv",
    "NaturalResourcesRents": "/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Natural Resources Rents/Clean Data/Cleaned_NaturalResources_data.csv",
    "WorldGovernance": "/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/World Governance/Clean Data/Cleaned_WorldwideGovernance_data.csv",
    "GDP": "/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Gross Domestic Product/Clean Data/Cleaned_GrossDomesticProduct_data.csv"
}

# Initialize an empty DataFrame
combined_data = pd.DataFrame()

# Load each file and merge into the combined DataFrame
for variable, file_path in file_paths.items():
    # Load the data for the current variable
    variable_data = pd.read_csv(file_path)
    
    # Ensure the variable data contains 'Country' and 'Data'
    variable_data.columns = ["Country", variable]  # Rename columns to 'Country' and the variable name
    
    # Merge with the combined DataFrame
    if combined_data.empty:
        combined_data = variable_data  # Initialize with the first variable
    else:
        combined_data = pd.merge(combined_data, variable_data, on="Country", how="inner")  # Merge on the 'Country' column

# Generate the scatter plot matrix
sns.set(style="whitegrid", font_scale=1.2)  # Clean grid style and larger font
pairplot = sns.pairplot(combined_data.iloc[:, 1:], diag_kind="kde", corner=True, height=2.5, aspect=1.2)

# Add title and adjust layout
plt.suptitle("Scatter Plot Matrix of Pre-Normalized Data", y=1.02, fontsize=16)
plt.subplots_adjust(top=0.95, hspace=0.3, wspace=0.3)

# Save the scatter plot as an image
scatter_plot_file = "Scatter_Plot_Matrix.png"
plt.savefig(scatter_plot_file, dpi=300)
plt.show()

# Calculate correlation coefficients
correlation_matrix = combined_data.iloc[:, 1:].corr()  # Exclude the 'Country' column

# Save correlation coefficients to a text file
correlation_file = "Correlation_Coefficients.txt"
with open(correlation_file, "w") as f:
    f.write("Correlation Coefficients\n")
    f.write("=========================\n\n")
    f.write(correlation_matrix.to_string())
    f.write("\n\nKey Observations:\n")
    f.write("- Correlation coefficients range from -1 (strong negative) to 1 (strong positive).\n")
    f.write("- Identify the strongest relationships for modeling.\n")

# Output confirmation messages
print(f"Scatter plot matrix saved as {scatter_plot_file}")
print(f"Correlation coefficients saved as {correlation_file}")
