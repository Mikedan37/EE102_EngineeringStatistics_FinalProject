import pandas as pd

def remove_blanks(input_file, output_file):
    """
    Reads a CSV file, removes rows with any missing values, 
    and saves the cleaned data to a new file.
    
    Parameters:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the cleaned CSV file.
    """
    # Load the data
    data = pd.read_csv(input_file)
    
    # Remove rows with blanks (NaN values) in any column
    cleaned_data = data.dropna()
    
    # Save the cleaned data to a new file
    cleaned_data.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

# Input and output file paths
input_file = "/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Linear Models/Data/Testing_Data.csv"  # Replace with your file path
output_file = "Blankless_Testing_Data.csv"  # Replace with your desired output file path

# Remove blanks and save the cleaned data
remove_blanks(input_file, output_file)
