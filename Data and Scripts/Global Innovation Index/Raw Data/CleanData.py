import pandas as pd

def clean_global_innovation_data(input_file, output_file):
    # Load the data
    data = pd.read_csv(input_file)

    # Filter rows where Attribute 1 is "Score"
    scores_data = data[data["Attribute 1"] == "Score"]

    # Extract data for the year 2016
    data_2016 = scores_data[["Economy Name", "2016"]].dropna()

    # Keep only the first score for each country
    unique_2016_data = data_2016.groupby("Economy Name").first().reset_index()

    # Rename columns for clarity
    unique_2016_data.rename(columns={"Economy Name": "Country", "2016": "Score"}, inplace=True)
    
    # Remove countries with a score of 0
    filtered_data = unique_2016_data[unique_2016_data["Score"] != 0]
    
    # Save the cleaned data to a CSV file
    filtered_data.to_csv(output_file, index=False)
    
    print(len(filtered_data))

input_file = '/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Global Innovation Index/Raw Data/GlobalInnovation_data.csv'
output_file = '/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Global Innovation Index/Clean Data/Cleaned_GlobalInnovation_data.csv'
clean_global_innovation_data(input_file, output_file)
    

 
