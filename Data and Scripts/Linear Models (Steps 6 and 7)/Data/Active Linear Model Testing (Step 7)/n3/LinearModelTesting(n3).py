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

# Define the n=3 model
model_name = ["GCI", "GII", "HCI"]
coefficients = [0.0078746, 0.00103562, 0.01298983]  # Replace with your model's coefficients
intercept = 0.01779478867765881  # Replace with your model's intercept

# Predict using the model
predictions = X_test.dot(coefficients) + intercept

# Calculate MSE and R²
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

# Save results to a text file
output_file = "N3_Model_Evaluation_Results.txt"
with open(output_file, "w") as txt_file:
    txt_file.write("N3 Model Evaluation Results\n")
    txt_file.write("===========================\n\n")
    txt_file.write(f"Model with input variables: {model_name}\n")
    txt_file.write(f"  Coefficients: {coefficients}\n")
    txt_file.write(f"  Intercept: {intercept}\n")
    txt_file.write(f"  Mean Squared Error (MSE): {mse}\n")
    txt_file.write(f"  R² (coefficient of determination): {r2}\n")

print(f"Evaluation results saved to {output_file}.")
