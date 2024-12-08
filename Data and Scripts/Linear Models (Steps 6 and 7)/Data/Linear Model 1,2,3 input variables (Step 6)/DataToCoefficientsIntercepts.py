import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from itertools import combinations

# Load the training and testing data
training_data_path = "/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Linear Models/Data/Used Data/Modeling_Data.csv"  # Replace with your training data file path
testing_data_path = "/Users/mdanylchuk/Desktop/EE102 Final Proj/Data and Scripts/Linear Models/Data/Used Data/Testing_Data.csv"  # Replace with your testing data file path

train_data = pd.read_csv(training_data_path)
test_data = pd.read_csv(testing_data_path)

# Define input and output columns
input_columns = ["GCI", "GII", "HCI"]  # Replace with actual input names
output_column = "GDP"  # Replace with actual output variable name

# Extract training inputs (X_train) and outputs (y_train)
X_train = train_data[input_columns]
y_train = train_data[output_column]

# Extract testing inputs (X_test) and outputs (y_test)
X_test = test_data[input_columns]
y_test = test_data[output_column]

# Fill missing values with the mean
X_train = X_train.fillna(X_train.mean())  # Fill missing values in training data
X_test = X_test.fillna(X_test.mean())    # Fill missing values in testing data

# Handle NaN values in target data
y_train = y_train.fillna(y_train.mean())
y_test = y_test.fillna(y_test.mean())

# Initialize a LinearRegression model
model = LinearRegression()

# Function to fit the model and test it
def fit_and_test_model(X_train_subset, y_train, X_test_subset, y_test, input_vars):
    model.fit(X_train_subset, y_train)
    coefficients = model.coef_
    intercept = model.intercept_
    predictions = model.predict(X_test_subset)
    mse = mean_squared_error(y_test, predictions)
    result = f"Model with input variables: {input_vars}\n"
    result += f"  Coefficients: {coefficients}\n"
    result += f"  Intercept: {intercept}\n"
    result += f"  Mean Squared Error on Test Data: {mse}\n\n"
    return result

# Open files for writing results
with open("n1_models.txt", "w") as n1_file, open("n2_models.txt", "w") as n2_file, open("n3_models.txt", "w") as n3_file:
    
    # 1. Models with one input variable (n=1)
    n1_file.write("Models with one input variable:\n")
    for input_var in input_columns:
        result = fit_and_test_model(X_train[[input_var]], y_train, X_test[[input_var]], y_test, [input_var])
        n1_file.write(result)

    # 2. Models with two input variables (n=2)
    n2_file.write("Models with two input variables:\n")
    for input_vars in combinations(input_columns, 2):
        result = fit_and_test_model(X_train[list(input_vars)], y_train, X_test[list(input_vars)], y_test, input_vars)
        n2_file.write(result)

    # 3. Models with three input variables (n=3)
    n3_file.write("Model with three input variables:\n")
    result = fit_and_test_model(X_train[input_columns], y_train, X_test[input_columns], y_test, input_columns)
    n3_file.write(result)

print("Results saved to n1_models.txt, n2_models.txt, and n3_models.txt.")
