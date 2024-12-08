import pandas as pd
from sklearn.model_selection import train_test_split

def split_data(input_file, modeling_file, testing_file, test_size=0.1, random_state=42):
    """
    Splits a dataset into modeling and testing sets.

    Parameters:
        input_file (str): Path to the input CSV file.
        modeling_file (str): Path to save the modeling dataset (90% of data).
        testing_file (str): Path to save the testing dataset (10% of data).
        test_size (float): Proportion of the dataset to include in the test split.
        random_state (int): Random seed for reproducibility.
    """
    # Load the dataset
    data = pd.read_csv(input_file)

    # Split the data
    modeling_data, testing_data = train_test_split(data, test_size=test_size, random_state=random_state)

    # Save the resulting datasets
    modeling_data.to_csv(modeling_file, index=False)
    testing_data.to_csv(testing_file, index=False)

    print(f"Modeling data saved to: {modeling_file}")
    print(f"Testing data saved to: {testing_file}")

# Example usage
input_file = "/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Human Capital Index/Normalized Data/Normalized_HumanCapital_data.csv"  # Replace with your actual file path
modeling_file = "Modeling_Data.csv"
testing_file = "Testing_Data.csv"

split_data(input_file, modeling_file, testing_file)
