import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from scipy.optimize import curve_fit

# Load test data
test_data_path = "/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Linear Models (Steps 6 and 7)/Data/Used Data/Testing_Data.csv"  # Replace with your test data file path
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

# Define the heuristic function
def heuristic_model(inputs, a, b, c, d, e):
    GCI, GII, HCI = inputs
    return a * GCI**2 + b * GII + c * HCI**2 + d * GCI * GII + e

# Prepare data for curve fitting
GCI = X_test["GCI"].values
GII = X_test["GII"].values
HCI = X_test["HCI"].values

# Initial guess for coefficients (a, b, c, d, e)
initial_guess = [0.01, 0.01, 0.01, 0.01, 0.01]

# Perform curve fitting
params, _ = curve_fit(heuristic_model, (GCI, GII, HCI), y_test, p0=initial_guess)

# Extract optimized coefficients
a, b, c, d, e = params

# Predict using the optimized heuristic model
y_pred = heuristic_model((GCI, GII, HCI), a, b, c, d, e)

# Calculate MSE for the heuristic model
mse_heuristic = mean_squared_error(y_test, y_pred)

# Save results to a text file
output_file = "Heuristic_Model_Evaluation.txt"
with open(output_file, "w") as txt_file:
    txt_file.write("Heuristic Model Evaluation Results\n")
    txt_file.write("==================================\n\n")
    txt_file.write("Heuristic Model: f(GCI, GII, HCI) = a * GCI^2 + b * GII + c * HCI^2 + d * GCI * GII + e\n")
    txt_file.write(f"  Optimized Coefficients:\n")
    txt_file.write(f"    a: {a}\n")
    txt_file.write(f"    b: {b}\n")
    txt_file.write(f"    c: {c}\n")
    txt_file.write(f"    d: {d}\n")
    txt_file.write(f"    e: {e}\n")
    txt_file.write(f"\n  Mean Squared Error (MSE): {mse_heuristic}\n")

print(f"Heuristic model evaluation results saved to {output_file}.")
print("Optimized Coefficients:")
print(f"  a: {a}, b: {b}, c: {c}, d: {d}, e: {e}")
print(f"  MSE: {mse_heuristic}")
