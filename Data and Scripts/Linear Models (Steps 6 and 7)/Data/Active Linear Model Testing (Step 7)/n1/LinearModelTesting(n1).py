import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score

# Load the test data
test_data_path = "/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Linear Models/Data/Used Data/Testing_Data.csv"  # Replace with your test data file path
test_data = pd.read_csv(test_data_path)

# Define input and output columns
input_columns = ["GCI", "GII", "HCI"]  # Replace with actual input names
output_column = "GDP"  # Replace with actual output variable name

# Extract test inputs (X_test) and outputs (y_test)
X_test = test_data[input_columns]
y_test = test_data[output_column]

# Fill missing values in X_test and y_test with their column means
X_test = X_test.fillna(X_test.mean())
y_test = y_test.fillna(y_test.mean())

# Define your models (coefficients and intercepts from Step 6)
models = {
    "GCI": {"coefficients": [0.01687566], "intercept": 0.019200235912278547},
    "GII": {"coefficients": [0.01582294], "intercept": 0.019673167015119113},
    "HCI": {"coefficients": [0.016152], "intercept": 0.021535306800049128},
    # Add more models if you have combinations of two or three variables
}

# Open a text file for saving the results
with open("N1_Model_Evaluation_Results.txt", "w") as txt_file:
    # Header for the text file
    txt_file.write("N1 Model Evaluation Results\n")
    txt_file.write("=========================\n\n")

    # Evaluate each model
    for model_name, params in models.items():
        coefficients = params["coefficients"]
        intercept = params["intercept"]
        
        # Predict using the model
        if len(coefficients) == 1:  # Single variable models
            predictions = X_test[[model_name]].values.flatten() * coefficients[0] + intercept
        else:  # Multi-variable models
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

print("Evaluation results saved to N1_Model_Evaluation_Results.txt.")
