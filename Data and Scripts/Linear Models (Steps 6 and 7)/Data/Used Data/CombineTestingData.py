import pandas as pd

def combine_files(file_paths, output_file_path):
    """
    Combines 5 input CSV files (Country, Data) into a single CSV file with Country as the first column
    and each subsequent column containing data from the respective file.
    
    Parameters:
    - file_paths: List of file paths to the input CSV files.
    - output_file_path: Path to the output CSV file.
    """
    combined_data = None

    for i, file_path in enumerate(file_paths):
        # Read the current file
        data = pd.read_csv(file_path)

        # Ensure the file has exactly two columns: Country and Data
        if len(data.columns) != 2:
            raise ValueError(f"File {file_path} must contain exactly two columns: 'Country' and 'Data'.")

        # Rename the data column to make it unique
        column_name = f"Data{i + 1}"
        # Define column names for each index
        if i == 0:
            column_name = "GCI"  # Global Competitiveness Index
        elif i == 1:
            column_name = "GII"  # Global Innovation Index
        elif i == 2:
            column_name = "GDP"  # Gross Domestic Product
        elif i == 3:
            column_name = "HCI"  # Human Capital Index
        elif i == 4:
            column_name = "NRR"  # Natural Resources Rents
        elif i == 5:
            column_name = "WGI"  # World Governance Index
        else:
            raise ValueError(f"Invalid index value: {i}")
        data.columns = ["Country", column_name]

        # Merge with the combined DataFrame
        if combined_data is None:
            combined_data = data  # Initialize with the first file
        else:
            combined_data = pd.merge(combined_data, data, on="Country", how="outer")

    # Save the combined data to a CSV file
    combined_data.to_csv(output_file_path, index=False)
    print(f"Combined data saved to {output_file_path}")

# Define the file paths to your 5 data files
file_paths = [
    "/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Global Competitiveness Index/Normalized Data/Model:Test/Testing_Data.csv",
    "/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Global Innovation Index/Normalized Data/Model:Test/Testing_Data.csv",
    "/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Gross Domestic Product/Normalized Data/Model:Test/Testing_Data.csv",
    "/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Human Capital Index/Normalized Data/Model:Test/Testing_Data.csv",
    "/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Natural Resources Rents/Normalized Data/Model:Test/Testing_Data.csv",
    "/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/World Governance/Normalized Data/Model:Test/Testing_Data.csv"
]

# Define the output file path
output_file_path = "Testing_Data.csv"  # Replace with your desired output file path

# Combine the files into a single CSV
combine_files(file_paths, output_file_path)
