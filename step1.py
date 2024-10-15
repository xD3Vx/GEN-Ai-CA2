import pandas as pd
# Load the Excel file
file_path = 'Auto_Regressive_Model_Diffusion_Model_V_1.0.xlsx'
xls = pd.ExcelFile(file_path)

# Step 1: Create Symptom Dictionary
# Load the Base Data Set to create a symptom dictionary
base_data_set_full = pd.read_excel(xls, sheet_name='Base_Data_Set')

# Assuming symptom severity is classified across columns, we'll create a dictionary
symptom_dict = {
    'Symptom 1': ['Fever: mild, low, high'],
    'Symptom 2': ['Cough: mild, low, high'],
    'Symptom 3': ['Cold: mild, low, high']
}

# Display the symptom dictionary
print("Symptom Dictionary:")
print(symptom_dict)
