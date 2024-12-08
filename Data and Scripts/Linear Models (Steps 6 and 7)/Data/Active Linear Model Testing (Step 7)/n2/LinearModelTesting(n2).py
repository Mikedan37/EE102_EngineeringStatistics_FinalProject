import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score

# Load the test data
test_data_path = "/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Linear Models/Data/Used Data/Testing_Data.csv"  # Replace with your test data file path
test_data = pd.read_csv(test_data_path)

# Define input and output columns
input_columns = ["GCI", "GII", "HCI"]
output_column = "GDP"

# Extract test inputs (X_test) and outputs (y_test)
X_test = test_data[input_columns]
y_test = test_data[output_column]

# Preprocess test data to handle NaN values
X_test = X_test.fillna(X_test.mean())
y_test = y_test.fillna(y_test.mean())

# Define models for n=2 (two-variable combinations)
models = {
    ("GCI", "GII"): {"coefficients": [0.01164111, 0.00899798], "intercept": 0.016921753572956465},
    ("GCI", "HCI"): {"coefficients": [0.00829155, 0.01327677], "intercept": 0.018031775608982614},
    ("GII", "HCI"): {"coefficients": [0.00471461, 0.0141875], "intercept": 0.019654391773786146},
}

# Open a text file to save the results
with open("N2_Model_Evaluation_Results.txt", "w") as txt_file:
    # Header for the text file
    txt_file.write("N2 Model Evaluation Results\n")
    txt_file.write("===========================\n\n")

    # Evaluate each model
    for model_name, params in models.items():
        coefficients = params["coefficients"]
        intercept = params["intercept"]

        # Predict using the model
        predictions = X_test[list(model_name)].dot(coefficients) + intercept

        # Calculate MSE and R²
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)

        # Write the results to the text file
        txt_file.write(f"Model: {model_name}\n")
        txt_file.write(f"  Coefficients: {coefficients}\n")
        txt_file.write(f"  Intercept: {intercept}\n")
        txt_file.write(f"  Mean Squared Error (MSE): {mse}\n")
        txt_file.write(f"  R² (coefficient of determination): {r2}\n\n")

print("Evaluation results saved to N2_Model_Evaluation_Results.txt.")
