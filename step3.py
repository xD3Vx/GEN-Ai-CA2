import pandas as pd

# Step 1: Load the file
file_path = 'Auto_Regressive_Model_Diffusion_Model_V_1.0.xlsx'
xls = pd.ExcelFile(file_path)

# Read the 'Base_Data_Set' sheet into a DataFrame
base_data_set_full = pd.read_excel(xls, sheet_name='Base_Data_Set')

# Check the DataFrame columns
print("Columns in the DataFrame:")
print(base_data_set_full.columns.tolist())

# Ensure the correct column names are used
# Proceed only if 'Observation' and other expected columns are present
if 'Observation' in base_data_set_full.columns and 'Patient_Id' in base_data_set_full.columns:
    # Step 2: Print the Loss (missing attributes in dataset) and the Enhanced Dictionary
    loss_entries = base_data_set_full[base_data_set_full['Observation'].isna()]

    print("Loss (Missing Observations):")
    print(loss_entries[['SrNo', 'Patient_Id', 'Observation', 'Particulars']])

    # Dictionary from previous steps
    symptom_dict = {
        'S1': {'Fever: mild', 'Fever: low', 'Fever: high'},
        'S2': {'Cough: mild', 'Cough: low', 'Cough: high'},
        'S3': {'Cold: mild', 'Cold: low', 'Cold: high'},
        'S4': {'Body Ache'},
        'S5': {'Cold'},
        'S6': {'Shivering: mild', 'Shivering: high', 'Shivering: Intermittent'}
    }

    # Step 3.1: Print the Enhanced Dictionary
    print("\nEnhanced Symptom Dictionary:")
    for key, value in symptom_dict.items():
        print(f"{key}: {value}")

    # Attach attributes to dictionary elements
    attributes = [
        {'Patient_Id': '000000001', 'Particulars': 'Low Body Ache, High Head Ache', 'Time Period': 'In Morning', 'City': 'City1', 'State': 'State1', 'Country': 'Country1', 'Pincode': '111111'},
        {'Patient_Id': '000000002', 'Particulars': 'High Shivering', 'Time Period': 'In Afternoon', 'City': 'City2', 'State': 'State2', 'Country': 'Country2', 'Pincode': '222222'},
        {'Patient_Id': '000000003', 'Particulars': 'Low Nausia', 'Time Period': 'Throughout', 'City': 'City3', 'State': 'State3', 'Country': 'Country3', 'Pincode': '333333'},
        {'Patient_Id': '000000004', 'Particulars': 'No observation', 'Time Period': 'No observation', 'City': 'No observation', 'State': 'No observation', 'Country': 'No observation', 'Pincode': 'No observation'},
    ]

    #Attach these attributes to the dictionary based on patient data
    for attribute in attributes:
        patient_id = attribute['Patient_Id']
        observation = base_data_set_full[base_data_set_full['Patient_Id'] == patient_id]['Observation'].values[0]

        if observation in symptom_dict.keys():
            # Attach the attributes to the dictionary
            symptom_dict[observation] = {
                'Particulars': attribute['Particulars'],
                'Time Period': attribute['Time Period'],
                'Location': {
                    'City': attribute['City'],
                    'State': attribute['State'],
                    'Country': attribute['Country'],
                    'Pincode': attribute['Pincode']
                }
            }

    # Check for loss of attributes
    loss_of_attributes = 0

    for symptom, details in symptom_dict.items():
        if not isinstance(details, dict):  # If it's still a set (no attributes attached), count it as a loss
            loss_of_attributes += 1

    # Output the final dictionary and loss of attributes
    print("\nEnhanced Symptom Dictionary with Attributes:")
    for key, value in symptom_dict.items():
        print(f"{key}: {value}")

    print(f"\nLoss of Attributes: {loss_of_attributes}")
else:
    print("Required columns are missing in the DataFrame.")
